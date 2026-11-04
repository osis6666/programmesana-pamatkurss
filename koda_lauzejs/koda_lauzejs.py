# 7.6 Koda lauzejs - 1.-3. uzdevums un papildu uzdevums vienā failā.
# Moduļu versija (pilnais nodevums) ir engine.py + main.py.

apaksa = 1
augsa = 100
minejumi = 0

print(f"Iedomājies skaitli no {apaksa} līdz {augsa}.")
print(f"Pirmais minējums būs {(apaksa + augsa) // 2}.")

while True:
    # Papildu uzdevums: ja robežas sagājušas pāri, atbildes bija pretrunīgas
    if apaksa > augsa:
        print("Atbildes ir bijušas pretrunīgas - tāda skaitļa nav!")
        break

    minejums = (apaksa + augsa) // 2
    minejumi += 1
    atbilde = input(f"Vai tavs skaitlis ir {minejums}? (lielaks/mazaks/pareizi): ")
    atbilde = atbilde.strip().lower()

    if atbilde == "lielaks":
        apaksa = minejums + 1
    elif atbilde == "mazaks":
        augsa = minejums - 1
    elif atbilde == "pareizi":
        print(f"Uzminēju! Vajadzēja {minejumi} minējumus.")
        break
    else:
        print("Neizpratu atbildi, raksti lielaks, mazaks vai pareizi.")
        minejumi -= 1  # nederīga ievade nav minējums
