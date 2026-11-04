# Testu pieraksts

Visas partijas izspēlētas ar `main.py`, diapazons 1-100. Kolonna "Minējumi" ir datora secība.

## Godīgas partijas

| Iedomātais skaitlis | Atbildes | Minējumi | Rezultāts |
|---|---|---|---|
| 73 | L M L L L U | 50, 75, 62, 68, 71, 73 | Uzvara 6 gājienos |
| 1 | M M M M M U | 50, 25, 12, 6, 3, 1 | Uzvara 6 gājienos |
| 100 | L L L L L L U | 50, 75, 88, 94, 97, 99, 100 | Uzvara 7 gājienos |

Lielākais minējumu skaits: **7** (skaitlis 100). Lineārā stratēģija sliktākajā gadījumā prasītu **100** minējumus.

Pārbaude visiem skaitļiem: `speletajs_auto()` izspēlēja visus 100 skaitļus. Maksimums ir 7 gājieni (tik vajag 37 skaitļiem), vidēji 5,80. Diapazonam 1-1000 maksimums ir 10, vidēji 8,99.

## Nederīga ievade

| Ievade | Programmas reakcija |
|---|---|
| `jā` | "Raksti L (lielāks), M (mazāks) vai U (uzminēji)." un jautā to pašu minējumu vēlreiz |
| `  L ` | Pieņem kā `L` (`.strip().lower()`) |

## Pretrunīgas spēles (krāpšanās)

**1. spēle, `main.py`.** Iedomāts 73, bet pēc pareizā minējuma turpinu melot ar "lielāks".

| Minējums | 50 | 75 | 62 | 68 | 71 | 73 | 74 |
|---|---|---|---|---|---|---|---|
| Atbilde | L | M | L | L | L | L (meli) | L |
| Robežas pēc tam | 51-100 | 51-74 | 63-74 | 69-74 | 72-74 | 74-74 | 75-74 |

Rezultāts: `Krāpšanās! Pēc 7 atbildēm neviens skaitlis tām visām neatbilst.` Robežas 75-74 ir neiespējamas, spēle beidzas.

**2. spēle, `koda_lauzejs.py`.** Atbildes: lielaks, mazaks, mazaks, lielaks, lielaks, lielaks, lielaks (minējumi 50, 75, 62, 56, 59, 60, 61). Pēc "mazāks par 62" un "lielāks par 61" neviens skaitlis neder.

Rezultāts: `Atbildes ir bijušas pretrunīgas - tāda skaitļa nav!`

Abos gadījumos programma apstājas, nevis iestrēgst bezgalīgā ciklā.
