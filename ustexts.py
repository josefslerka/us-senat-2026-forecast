"""US 2026 Senate public site texts (cs)."""

TITLE = "USA 2026: Senát — veřejný experiment s AI forecastingem"
LEAD = ("Pravděpodobnostní předpověď voleb do Senátu USA 3. 11. 2026: devět senátních závodů a kontrola Senátu a Sněmovny. "
        "Čistá AI bez kurzů a bez volebních modelů, vedle ní sázkové kurzy, profesionální volební model a jejich srovnání. "
        "Po volbách vše vyhodnotíme podle předem zveřejněných pravidel.")

STATUS_BOX = """<div class="card" style="border-left:4px solid var(--accent)"><h2 style="margin-top:0">Co je dnes nového · út 27. 10. 2026, {TIME}</h2>
<ul>
<li><b>AI předpovědi pro všech 11 otázek jsou hotové</b>, zamčené ve 21:09. Kurzy a model jsme četli až potom.</li>
<li><b>Všechny série mají stejného favorita</b> v 11 z 11 otázek.</li>
<li><b>AI je opatrnější než sázky</b> v 9 z 11, stejně jako u Senátu ČR a na Slovensku. Víc než sázky věří favoritovi jen v Iowě (Hinson 69 % proti 57 %); v Nebrasce jsou skoro stejně.</li>
<li><b>AI je blízko modelu The Economist:</b> v 6 z 11 otázek do 2,5 bodu. Nejvíc se liší v Nebrasce (Ricketts: AI 72 %, model 84 %) a u Sněmovny (85 % proti 95 %).</li>
<li>Hodnotí se verze zamčená v pondělí 2. 11. ve 12:00. Do té doby AI měníme jen při novém faktu.</li>
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
<h2>Út 27. 10. 2026 večer: den 0, první předpovědi</h2>
<h3>Co se stalo</h3><ul>
<li>20:26 pravidla (předregistrace), 20:35 oficiální seznamy kandidátů, 20:43 sdílený soubor průzkumů, ratingů a přesnosti agentur. Časy podle commitů.</li>
<li>Čtyři skupiny agentů prošly celou pipeline pro 11 otázek. Zamčeno ve 21:09.</li>
<li>Pak jsme přečetli kurzy Tipsportu (9 států a kombinace Senát/Sněmovna) a Fortuny (kombinace) a data modelu The Economist.</li></ul>
<h3>Co vidíme</h3><ul>
<li><b>Stejný favorit všude.</b> Liší se jen jistota.</li>
<li><b>K sázkám:</b> AI je opatrnější v 9 z 11, nejvíc v Minnesotě (77 % proti 91 %) a u kontroly Senátu (60 % proti 70 %). <b>Od sázek:</b> v Iowě dává AI Hinsonovi víc (69 % proti 57 %).</li>
<li><b>K modelu:</b> v šesti otázkách (Florida, Iowa, Jižní Karolína, Michigan, Minnesota, Ohio) se AI a model The Economist liší nejvýš o 2,5 bodu. Obě série stojí na stejných průzkumech, takže blízkost je čekaná. Zčásti ji ale mohou vysvětlovat i slovní kategorie modelů, které agenti zahlédli na Wikipedii (viz níže). <b>Od modelu:</b> Nebraska (AI 72 %, model 84 %), Sněmovna (85 % proti 95 %), Kansas a Texas (o 6 bodů).</li>
<li><b>Extremizovaná AI</b> mění pět otázek, kde AI dává favoritovi aspoň 70 %: Floridu, Jižní Karolínu, Minnesotu, Nebrasku a Sněmovnu. Většinou ji to přibližuje k sázkám i modelu, v Nebrasce je s 84 % nad sázkami (75 %).</li>
<li><b>Vnitřní konzistence AI:</b> předpověď kontroly Senátu si počítá vlastní čísla po státech a ta se od samostatných předpovědí liší o 1–6 bodů (např. Ohio 69 % proti 63 %). Necháváme to tak a po volbách se podíváme, která čísla byla blíž.</li></ul>
<h3>Možné ovlivnění (⚠ u všech 11 otázek)</h3><ul>
<li>Ve výsledcích vyhledávání se agentům objevovaly titulky stránek s kurzy a modely. V Kansasu researcher otevřel článek Newsweeku kvůli ratingu Sabato a v článku byla i cena z Polymarketu. Číslo nezapsal a forecaster ani red-team článek neviděli.</li>
<li>Wikipedie má u každého závodu tabulku, která míchá povolené slovní ratingy (Cook, Sabato, Inside Elections) se slovními kategoriemi modelů. Agenti ji viděli opakovaně. Čísla modelů v ní nejsou.</li>
<li>Do fází odhadu šel vždy jen očištěný brief bez těchto položek.</li></ul>
<h3>Chyby a nápravy</h3><ul>
<li><b>Posunuté sloupce v tabulkách průzkumů.</b> Ve 13 řádcích sdíleného souboru byla chybná marže (např. Michigan „+40“ místo +5). <i>Příčina:</i> převod tabulek z Wikipedie s prázdnými buňkami. <i>Náprava:</i> agenti marže přepočítali z podílů sami; soubor jsme po předpovědích opravili.</li>
<li><b>Tabulky predikcí na Wikipedii.</b> <i>Náprava:</i> pro denní updaty je agentům zakazujeme, ratingy berou jen ze sdíleného souboru.</li>
<li><b>Model Silver Bulletin je jen pro předplatitele.</b> <i>Náprava:</i> podle předem zapsaného pořadí bereme druhý, The Economist, který data zveřejňuje.</li></ul>
<h3>Nové zdroje dne</h3><ul>
<li>Model: <a href="https://www.economist.com/interactive/2026/us-midterms/prediction-model/senate">The Economist, Senát</a> · <a href="https://www.economist.com/interactive/2026/us-midterms/prediction-model/house">Sněmovna</a></li>
<li>Průzkumy a průměry: 270toWin, RealClearPolling, Wikipedie „2026 United States Senate election in &lt;stát&gt;“ (seznam se zdroji v <a href="https://github.com/josefslerka/us-senat-2026-forecast">repozitáři</a>)</li>
<li>Přesnost agentur: <a href="https://www.natesilver.net/p/pollster-ratings-silver-bulletin">Silver Bulletin pollster ratings</a></li></ul>
<h3>Co dál</h3><p>Denně projdeme zprávy a nové průzkumy. AI se mění jen při novém faktu, pořadí: update → zámek → kurzy a model. Freeze v pondělí 2. 11. ve 12:00, večer poslední čtení kurzů.</p>
<h2>Út 27. 10. 2026: den 0, start</h2>
<ul>
<li>Rozhodli jsme se pro třetí případovou studii: Senát USA. Zapsali jsme pravidla dřív, než vznikl jakýkoli odhad.</li>
<li>Vybrali jsme závody podle nabídky Tipsportu (11 států), Aljašku a Maine vynecháváme kvůli preferenčnímu hlasování.</li>
<li><b>Novinky proti Slovensku:</b> extremizovaná AI je poprvé veřejná série; přidáváme profesionální volební model jako srovnání;
AI musí ke každému státu uvést očekávané podíly hlasů; před prvním odhadem projdeme přesnost jednotlivých agentur;
poslední čtení kurzů plánujeme na večer před volbami, ne na ráno.</li>
</ul>
<h3>Co dál</h3><p>Oficiální seznamy kandidátů, průzkumy a přesnost agentur. Pak AI předpovědi.</p>"""

TABLE_NOTE = ("Pravděpodobnost, že vyhraje favorit AI. Extremizovaná AI: když AI dává favoritovi aspoň 70 %, posuneme ji dál od 50 % "
              "(α = √3). Model: The Economist. Sázky: Tipsport, u Senátu a Sněmovny průměr Tipsportu a Fortuny, po odečtení marže. "
              "⚠ U všech otázek agenti zahlédli titulky stránek s kurzy nebo modely, čísla nepoužili (viz deník).")
