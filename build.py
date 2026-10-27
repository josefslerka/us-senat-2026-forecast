"""US 2026 Senate: build the public static site into ../us-senat-2026-forecast.

usage: python3 scripts/us2026/build.py <time-HH:MM> [<ai-date> <market-date> <model-date>]
Public series: AI, AI extremizovaná, Model, Sázky, AI + sázky. Internal baseline and paper bets never go to the site.
"""
import csv, html, importlib.util, json, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = (ROOT / "../us-senat-2026-forecast").resolve()
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ustexts as T  # noqa: E402

_spec = importlib.util.spec_from_file_location("skbuild", ROOT / "scripts/sk2026/build.py")
_sk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sk)
CSS = _sk.CSS + """
table.r2 th.gs,table.r2 td.gs{border-left:1px solid var(--line);padding-left:10px}
table.r2 tr.grp th{text-transform:none;letter-spacing:0;font-size:13px;color:var(--fg);border-bottom:0;padding-bottom:0}
table.cards td b{white-space:nowrap}.sm-only{display:none}
@media (max-width:640px){table.cards thead{display:none}table.cards,table.cards tbody,table.cards tr,table.cards td{display:block;width:auto}
table.cards tr{border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:10px 0;background:var(--card)}
table.cards td{border:0;padding:3px 0;display:flex;justify-content:space-between;gap:12px;text-align:right}
table.cards td::before{content:attr(data-label);color:var(--muted);text-align:left}
table.cards td.head{font-weight:600;font-size:17px}table.cards td.head::before{content:none}}
"""
REPO = "https://github.com/josefslerka/us-senat-2026-forecast"


def page(title, body, desc):
    nav = '<a href="index.html">Přehled</a><a href="pravidla.html">Pravidla</a><a href="denik.html">Deník</a>'
    return (f'<!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><style>{CSS}</style></head><body><div class="wrap">'
            f'<header><a class="brand" href="index.html">USA 2026 · Senát · forecast</a><nav>{nav}</nav></header>{body}'
            f'<footer>Predikce generuje AI pipeline (Claude) s člověkem ve smyčce. Nejde o sázkové tipy. Obsah CC BY 4.0, kód MIT. · '
            f'<a href="{REPO}">GitHub</a></footer></div></body></html>')


def names():
    out = {"Democrats": "Demokraté", "Republicans": "Republikáni"}
    for r in csv.DictReader(open(ROOT / "data/us-2026/candidates.csv", encoding="utf-8")):
        out.setdefault(r["key"], r["name"].split()[-1])
    out.update({"ElSayed": "El-Sayed", "Graham": "Graham"})
    return out


def pc(p):
    return f"{int(p * 100 + 0.5)} %"


def table(ai_date, mk_date, mo_date):
    ai = json.loads((ROOT / f"data/us-2026/snapshots/{ai_date}-ai.json").read_text())["races"]
    ex = json.loads((ROOT / f"data/us-2026/snapshots/{ai_date}-ai-ext.json").read_text())["races"]
    mk = json.loads((ROOT / f"data/us-2026/market/{mk_date}.json").read_text())["races"]
    mo = json.loads((ROOT / f"data/us-2026/model/{mo_date}.json").read_text())["races"]
    nm = names()
    cols = [("AI", "gs"), ("AI extremizovaná", ""), ("Model (The Economist)", "gs"), ("Sázky", "gs"), ("AI + sázky", "gs")]
    rows = []
    for r, label in T.QUESTIONS:
        d = ai[r]["dist"]
        k = max(d, key=d.get)
        vals = [d[k], ex[r]["dist"][k], mo[r]["dist"].get(k, 0), mk[r]["market"][k], mk[r]["blend"][k]]
        flag = " ⚠" if ai[r].get("contamination_risk") == "possible" else ""
        cells = "".join(f'<td class="{c}" data-label="{html.escape(n)}"><span>{html.escape(nm.get(k, k))} <b>{pc(v)}</b></span></td>'
                        for (n, c), v in zip(cols, vals))
        rows.append(f'<tr><td class="head">{html.escape(label)}{flag}</td>{cells}</tr>')
    head = ('<thead><tr class="grp"><th></th><th class="gs" colspan="2">Naše předpovědi</th><th class="gs">Model</th>'
            '<th class="gs">Trh</th><th class="gs">Kombinace</th></tr><tr><th>Otázka</th>'
            + "".join(f'<th class="{c}">{html.escape(n)}</th>' for n, c in cols) + "</tr></thead>")
    return (f'<h2>Předpovědi (AI zamčená {ai_date[8:10].lstrip("0")}. 10. ve 21:09)</h2>'
            f'<p class="muted" style="font-size:14px">{T.TABLE_NOTE}</p>'
            f'<div class="scroll"><table class="cards r2">{head}<tbody>{"".join(rows)}</tbody></table></div>')


def main():
    tm = sys.argv[1]
    OUT.mkdir(exist_ok=True)
    tab = table(*sys.argv[2:5]) if len(sys.argv) >= 5 else ""
    if tab:
        ai_date, mk_date, mo_date = sys.argv[2:5]
        (OUT / "data").mkdir(exist_ok=True)
        for src, dst in [(f"data/us-2026/snapshots/{ai_date}-ai.json", f"{ai_date}-ai.json"),
                         (f"data/us-2026/snapshots/{ai_date}-ai-ext.json", f"{ai_date}-ai-ext.json"),
                         (f"data/us-2026/model/{mo_date}.json", f"{mo_date}-model.json"),
                         ("runs/_us-2026-polls-news.md", "polls-news.md"), ("data/us-2026/candidates.csv", "candidates.csv")]:
            shutil.copy(ROOT / src, OUT / "data" / dst)
        m = json.loads((ROOT / f"data/us-2026/market/{mk_date}.json").read_text())
        pub = {"date": m["date"], "devig": m["devig"], "rho": m["rho"],
               "races": {r: {"market": v["market"], "blend": v["blend"], "books": {b: x["dist"] for b, x in v["books"].items()}}
                         for r, v in m["races"].items()}}
        (OUT / "data" / f"{mk_date}-market.json").write_text(json.dumps(pub, ensure_ascii=False, indent=1))
    body = (f"<h1>{T.TITLE}</h1><p class=lead>{T.LEAD}</p>{T.STATUS_BOX.replace('{TIME}', tm)}{tab}{T.ABOUT}")
    (OUT / "index.html").write_text(page("USA 2026 · Senát", body, T.LEAD))
    (OUT / "pravidla.html").write_text(page("Pravidla · USA 2026", T.RULES, "Pravidla vyhodnocení"))
    (OUT / "denik.html").write_text(page("Deník · USA 2026", T.JOURNAL, "Deník experimentu"))
    print("built", OUT)


if __name__ == "__main__":
    main()
