"""US 2026 Senate public site texts (cs)."""

TITLE = "USA 2026: Senát — veřejný experiment s AI forecastingem"
LEAD = ("Pravděpodobnostní předpověď voleb do Senátu USA 3. 11. 2026: devět senátních závodů a kontrola Senátu a Sněmovny. "
        "Čistá AI bez kurzů a bez volebních modelů, vedle ní sázkové kurzy, profesionální volební model a jejich srovnání. "
        "Po volbách vše vyhodnotíme podle předem zveřejněných pravidel.")

STATUS_BOX = """<div class="card" style="border-left:4px solid var(--accent)"><h2 style="margin-top:0">Stav · út 27. 10. 2026, {TIME}</h2>
<ul>
<li><b>Pravidla jsou zapsaná</b> předem, před prvním odhadem (<a href="pravidla.html">Pravidla</a>).</li>
<li>Teď sbíráme oficiální seznamy kandidátů, průzkumy a údaje o přesnosti jednotlivých agentur.</li>
<li>Předpovědi AI zveřejníme během čtvrtka a pátku. Hodnotí se verze zamčená v pondělí 2. 11. ve 12:00.</li>
</ul>
<p style="margin-bottom:0"><a href="pravidla.html">Pravidla →</a> · <a href="denik.html">Deník →</a></p></div>"""

QUESTIONS = [
    ("us-sen-fl", "Florida (doplňovací volba)"), ("us-sen-ia", "Iowa"), ("us-sen-sc", "Jižní Karolína"),
    ("us-sen-ks", "Kansas"), ("us-sen-mi", "Michigan"), ("us-sen-mn", "Minnesota"), ("us-sen-ne", "Nebraska"),
    ("us-sen-oh", "Ohio (doplňovací volba)"), ("us-sen-tx", "Texas"),
    ("us-senate-control", "Kontrola Senátu"), ("us-house-control", "Kontrola Sněmovny reprezentantů"),
]

ABOUT = """<div class="card"><p><b>Co je to za experiment.</b> Zkoušíme, jak dobrým forecasterem může být AI agent. Každou předpověď
vytváří vícekroková AI pipeline (Claude): upřesnění otázky, rešerše, odhad, kontrola, že tvrzení stojí na zdrojích, oponentura
(red-team) a agregace. Člověk pipeline řídí a kontroluje, ale čísla nemění.</p>
<p><b>Proč „bez kurzů a bez modelů“.</b> AI nevidí sázkové kurzy, predikční trhy ani pravděpodobnosti z volebních modelů. Smí číst
průzkumy, jejich průměry a slovní hodnocení závodů. Díky tomu půjde po volbách změřit, jestli AI přidává informaci, nebo jen opakuje
trh či model.</p>
<p>Třetí případová studie po <a href="https://josefslerka.github.io/senat-2026-forecast/">Senátu ČR 2026</a> a
<a href="https://josefslerka.github.io/sk-volby-2026-forecast/">slovenských volbách 2026</a>.</p></div>"""

RULES = """<h1>Pravidla</h1><p class="lead">Zveřejněno před volbami. Předregistrace interně út 27. 10. 2026 ve 20:26, před prvním odhadem.</p>
<h2>Co předpovídáme</h2><ul>
<li><b>Devět senátních závodů</b>, které vypisuje sázková kancelář Tipsport: Florida (doplňovací), Iowa, Jižní Karolína, Kansas,
Michigan, Minnesota, Nebraska, Ohio (doplňovací) a Texas. Aljašku a Maine vynecháváme: mají preferenční hlasování a konečný výsledek
může přijít až po 10. 11.</li>
<li><b>Kontrolu Senátu</b>: demokraté potřebují 51 křesel (včetně nezávislých, kteří s nimi hlasují), republikánům stačí 50, protože
při rovnosti rozhoduje viceprezident.</li>
<li><b>Kontrolu Sněmovny reprezentantů</b>: většina je 218 křesel.</li></ul>
<p>Každá předpověď závodu je rozdělení pravděpodobnosti mezi kandidáty z oficiálního seznamu, včetně položky „ostatní“.
Vítěze bereme podle vyhlášení agentury AP, při sporu podle certifikovaného výsledku.</p>
<h2>Série</h2><ul>
<li><b>AI</b>: čistá AI pipeline bez kurzů, predikčních trhů a pravděpodobností z modelů. Mění se jen při novém faktu.</li>
<li><b>AI extremizovaná</b>: když si AI dává favorita aspoň na 70 %, posuneme odhad dál od 50 % (p<sub>i</sub>′ ∝ p<sub>i</sub><sup>α</sup>,
α = √3). Parametry jsme zvolili po Senátu ČR a beze změny použili na Slovensku, tady je testujeme podruhé.</li>
<li><b>Sázky</b>: Tipsport (závody, Senát, Sněmovna) a Fortuna (Senát, Sněmovna), po odečtení marže (power de-vig), průměr kanceláří.</li>
<li><b>AI + sázky</b>: log-odds průměr AI a sázek (ρ = 0,55, stejně jako dřív).</li>
<li><b>Model</b>: jeden profesionální kvantitativní volební model. Bereme první, který ke dni freeze zveřejňuje pravděpodobnosti pro
všech devět států a kontrolu Senátu, v pořadí Silver Bulletin, The Economist, Split Ticket, Race to the WH.</li></ul>
<h2>Hodnocená předpověď</h2><p>AI: poslední zamčená verze před pondělím 2. 11. 2026 12:00 (SEČ). Sázky a model: přečtené po tomto zámku,
nejpozději ve 13:00. Večer 2. 11. přečteme sázky a model ještě jednou jako referenci před otevřením místností.</p>
<h2>Metriky</h2><p>Hlavní metrika: Brierovo skóre proti vítězi (součet přes všechny výstupy). Dál logaritmické skóre a trefa favorita.
Nově měříme i odhad náskoku: AI ke každému státu uvádí očekávané podíly hlasů a porovnáme, jestli se v náskoku vítěze spletla méně
než průměr průzkumů. Vzorek je malý, rozdíly budeme formulovat opatrně a vždy s počtem závodů.</p>
<h2>Pořadí každý den</h2><p>Zprávy → případný update AI → zamknutí → teprve potom kurzy a model.</p>"""

JOURNAL = """<h1>Deník</h1>
<h2>Út 27. 10. 2026: den 0, start</h2>
<ul>
<li>Rozhodli jsme se pro třetí případovou studii: Senát USA. Zapsali jsme pravidla dřív, než vznikl jakýkoli odhad.</li>
<li>Vybrali jsme závody podle nabídky Tipsportu (11 států), Aljašku a Maine vynecháváme kvůli preferenčnímu hlasování.</li>
<li><b>Novinky proti Slovensku:</b> extremizovaná AI je poprvé veřejná série; přidáváme profesionální volební model jako srovnání;
AI musí ke každému státu uvést očekávané podíly hlasů; před prvním odhadem projdeme přesnost jednotlivých agentur;
poslední čtení kurzů plánujeme na večer před volbami, ne na ráno.</li>
</ul>
<h3>Co dál</h3><p>Oficiální seznamy kandidátů, průzkumy a přesnost agentur. Pak AI předpovědi.</p>"""
