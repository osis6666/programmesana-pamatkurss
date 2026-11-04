"""Binārās meklēšanas dzinējs spēlei "Koda lauzējs"."""


def aprekinat_minejumu(apaksa, augsa):
    """Aprēķina viduspunktu binārajai meklēšanai."""
    return (apaksa + augsa) // 2


def atjaunot_robezas(apaksa, augsa, minejums, atbilde):
    """Atgriež jaunās robežas (apaksa, augsa) pēc spēlētāja atbildes.

    atbilde: "l" - skaitlis ir lielāks, "m" - skaitlis ir mazāks.
    Robeža pārvietojas vienu pozīciju aiz minējuma, citādi cikls var
    griezties mūžīgi uz viena un tā paša skaitļa.
    """
    if atbilde == "l":
        return minejums + 1, augsa
    if atbilde == "m":
        return apaksa, minejums - 1
    return apaksa, augsa


def ir_pretruna(apaksa, augsa):
    """True, ja neviens skaitlis vairs neatbilst visām atbildēm."""
    return apaksa > augsa


def max_minejumi(n):
    """Cik minējumu sliktākajā gadījumā vajag n skaitļiem: ceil(log2(n + 1))."""
    return n.bit_length()


def nosaukt_atbildi(slepenais, minejums):
    """Godīga spēlētāja atbilde - izmanto testos."""
    if slepenais > minejums:
        return "l"
    if slepenais < minejums:
        return "m"
    return "u"


def speletajs_auto(slepenais, apaksa=1, augsa=100):
    """Izspēlē partiju ar godīgu spēlētāju un atgriež minējumu skaitu."""
    gajieni = 0
    while not ir_pretruna(apaksa, augsa):
        minejums = aprekinat_minejumu(apaksa, augsa)
        gajieni += 1
        atbilde = nosaukt_atbildi(slepenais, minejums)
        if atbilde == "u":
            return gajieni
        apaksa, augsa = atjaunot_robezas(apaksa, augsa, minejums, atbilde)
    return None
