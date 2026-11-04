"""Koda lauzējs: dators ar bināro meklēšanu uzmin spēlētāja skaitli."""

from engine import aprekinat_minejumu, atjaunot_robezas, ir_pretruna, max_minejumi

DERIGAS = {"l": "l", "lielaks": "l", "m": "m", "mazaks": "m", "u": "u", "pareizi": "u"}


def nolasit_atbildi(minejums):
    """Jautā, līdz spēlētājs ievada L, M vai U."""
    while True:
        teksts = input(f"Vai tavs skaitlis ir {minejums}? (L/M/U): ").strip().lower()
        if teksts in DERIGAS:
            return DERIGAS[teksts]
        print("Raksti L (lielāks), M (mazāks) vai U (uzminēji).")


def spele(min_r=1, max_r=100):
    """Viena partija. Atgriež minējumu skaitu vai None, ja spēlētājs krāpās."""
    print(f"Iedomājies skaitli no {min_r} līdz {max_r}.")
    print(f"Man vajadzēs ne vairāk kā {max_minejumi(max_r - min_r + 1)} minējumus.")
    gajieni = 0

    while not ir_pretruna(min_r, max_r):
        minejums = aprekinat_minejumu(min_r, max_r)
        gajieni += 1
        atbilde = nolasit_atbildi(minejums)

        if atbilde == "u":
            print(f"Uzvara {gajieni} gājienos!")
            return gajieni
        min_r, max_r = atjaunot_robezas(min_r, max_r, minejums, atbilde)

    print(f"Krāpšanās! Pēc {gajieni} atbildēm neviens skaitlis tām visām neatbilst.")
    return None


if __name__ == "__main__":
    spele()
