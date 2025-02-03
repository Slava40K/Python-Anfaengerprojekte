# Galgenmännchen Spiel

import random

# Wortliste und zufällige Auswahl
liste = ["Apfel", "Straße", "Maus", "Bremse", "Pumpe"]  # einfachheitshalber nur eine sehr limitierte Wortwahl
wort = random.choice(liste).lower()
wort_verdeckt = "_" * len(wort)  # Wort verdeckt anzeigen mit Unterstrichen

# Counter-variablen um anzahl von verbleibenden Versuchen tracken
max_versuche = 6
versuche = 0
buchstaben_raten = []  # Um die geratenen Buchstaben zu speichern

# Spiel-Schleife
while versuche < max_versuche and "_" in wort_verdeckt:
    print("\nAktueller Stand: ", wort_verdeckt)
    buchstabe = input("Buchstaben eingeben: ").lower()
    
    # if statement um Nutzer darauf hinzuweisen, falls er bestimmten Buchstaben schon geraten hat
    if buchstabe in buchstaben_raten:
        print("Diesen Buchstaben hast du schon geraten!")
        continue

    buchstaben_raten.append(buchstabe)
    
    # Spiellogik, für den Fall richtiger oder falscher Rateversuche
    if buchstabe in wort:
        print(f"Der Buchstabe {buchstabe} ist im Wort!")
        wort_verdeckt = "".join([buchstabe if wort[i] == buchstabe else wort_verdeckt[i] for i in range(len(wort))])
    else:
        versuche += 1
        print(f"Der Buchstabe {buchstabe} ist nicht im Wort! Du hast noch {max_versuche - versuche} Versuche.")
        
# conditional statements um Sieg oder Niederlage zu ermitteln
if "_" not in wort_verdeckt:
    print(f"Herzlichen Glückwunsch! Du hast das Wort '{wort}' erraten!")
else:
    print(f"Leider verloren! Das Wort war '{wort}'.")
