"""US 2026 Senate: build the public static site into ../us-senat-2026-forecast.

usage: python3 scripts/us2026/build.py <time-HH:MM>
Stage 0 (before forecasts): status box, question list, rules, journal.
"""
import html, importlib.util, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = (ROOT / "../us-senat-2026-forecast").resolve()
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ustexts as T  # noqa: E402

_spec = importlib.util.spec_from_file_location("skbuild", ROOT / "scripts/sk2026/build.py")
_sk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sk)
CSS = _sk.CSS
REPO = "https://github.com/josefslerka/us-senat-2026-forecast"


def page(title, body, desc):
    nav = '<a href="index.html">Přehled</a><a href="pravidla.html">Pravidla</a><a href="denik.html">Deník</a>'
    return (f'<!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><style>{CSS}</style></head><body><div class="wrap">'
            f'<header><a class="brand" href="index.html">USA 2026 · Senát · forecast</a><nav>{nav}</nav></header>{body}'
            f'<footer>Predikce generuje AI pipeline (Claude) s člověkem ve smyčce. Nejde o sázkové tipy. Obsah CC BY 4.0, kód MIT. · '
            f'<a href="{REPO}">GitHub</a></footer></div></body></html>')


def main():
    tm = sys.argv[1]
    OUT.mkdir(exist_ok=True)
    qs = "".join(f"<li>{html.escape(n)}</li>" for _, n in T.QUESTIONS)
    body = (f"<h1>{T.TITLE}</h1><p class=lead>{T.LEAD}</p>{T.STATUS_BOX.replace('{TIME}', tm)}"
            f"<h2>Otázky</h2><ul>{qs}</ul>{T.ABOUT}")
    (OUT / "index.html").write_text(page("USA 2026 · Senát", body, T.LEAD))
    (OUT / "pravidla.html").write_text(page("Pravidla · USA 2026", T.RULES, "Pravidla vyhodnocení"))
    (OUT / "denik.html").write_text(page("Deník · USA 2026", T.JOURNAL, "Deník experimentu"))
    print("built", OUT)


if __name__ == "__main__":
    main()
