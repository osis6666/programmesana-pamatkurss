# Koda lauzējs: AI efektivitāte

7. tēmas noslēguma projekts. Tu iedomājies skaitli, dators to uzmin ar binārās meklēšanas stratēģiju un pamana, ja atbildes ir pretrunīgas.

## Palaišana

No krātuves saknes:

    cd koda_lauzejs
    python main.py

Uz katru minējumu atbildi ar `L` (tavs skaitlis ir lielāks), `M` (mazāks) vai `U` (uzminēji). Lielie vai mazie burti un atstarpes nav svarīgi; citu ievadi programma prasa vēlreiz.

`koda_lauzejs.py` ir tā pati spēle vienā failā, kā to būvē stundas 1.-3. uzdevumā (atbildes `lielaks` / `mazaks` / `pareizi`).

## Struktūra

- `engine.py` - dzinējs: `aprekinat_minejumu()`, `atjaunot_robezas()`, `ir_pretruna()`, `max_minejumi()` un automātiskais godīgais spēlētājs testiem
- `main.py` - spēle ar ievadi un izvadi
- `koda_lauzejs.py` - stundas versija vienā failā
- `testi.md` - izspēlēto partiju pieraksts

## Algoritms

Dators tur divas robežas: `apaksa` un `augsa`. Katrā gājienā tas min vidu `(apaksa + augsa) // 2`.

- Atbilde `L` → `apaksa = minejums + 1`
- Atbilde `M` → `augsa = minejums - 1`

Robeža pāriet **vienu pozīciju aiz** minējuma, jo pats minējums jau ir izslēgts. Ja to neizdarītu, dators varētu mūžīgi minēt vienu un to pašu skaitli.

**Pretruna (krāpšanās).** Ja pēc atbildes `apaksa > augsa`, diapazonā vairs nav neviena skaitļa, kas atbilstu visām atbildēm, tātad vismaz viena no tām bija nepatiesa. Spēle to paziņo un beidzas, nevis griežas bezgalīgā ciklā.

## Efektivitāte: O(log n)

Pēc katra minējuma paliek ne vairāk kā puse no iepriekšējiem variantiem. Ar `k` minējumiem binārā meklēšana var atšķirt ne vairāk kā `2^k - 1` skaitli, tāpēc sliktākajā gadījumā vajag

    k = ⌈log₂(n + 1)⌉

minējumus. Lineārā meklēšana (1, 2, 3, ...) sliktākajā gadījumā prasa `n` minējumus, tas ir O(n).

| Skaitļu diapazons | Binārā, sliktākais | Binārā, vidēji | Lineārā, sliktākais |
|---|---|---|---|
| 1-100 | 7 | 5,80 | 100 |
| 1-1000 | 10 | 8,99 | 1000 |

Binārās meklēšanas skaitļi ir **izmērīti**, nevis tikai izrēķināti: `engine.speletajs_auto()` izspēlēja partiju ar katru skaitli 1-100 un 1-1000. Maksimums sakrita ar formulu: 7 un 10. Ja diapazonu palielina 10 reizes, binārajai vajag tikai par ~3 minējumiem vairāk, bet lineārajai 10 reizes vairāk.

Pārbaudīt pašam:

    python -c "from engine import speletajs_auto; print(max(speletajs_auto(s) for s in range(1, 101)))"

## Testi

Skatīt [testi.md](testi.md): trīs godīgas partijas (73, 1, 100), nederīga ievade un divas pretrunīgas spēles, kurās programma pamana krāpšanos.
