# einfacher Taschenrechner mit Addition, Subtraktion, Multiplikation, Division
# von 2 Zahlen

# Funktionen für verschiedene Rechenoperationen
def addition(zahl_1, zahl_2):
    return zahl_1 + zahl_2
def subtraktion(zahl_1, zahl_2):
    return zahl_1 - zahl_2
def multiplikation(zahl_1, zahl_2):
    return zahl_1 * zahl_2
def division(zahl_1, zahl_2):
    # Errorhandling im Falle der Division durch 0
    if zahl_2 == 0:
        print("kann nicht durch 0 teilen.")
        return None
    return zahl_1 / zahl_2

# HAUPTTEIL
# while schleife um Rechenoperation zu wählen oder Programm zu beenden.
while True:
    wahl = input("\nBitte Rechenoperation mit entsprächender Zahl wählen:\n"
    "\n1. Addition\n"
    "2. Subtraktion\n"
    "3. Multiplikation\n"
    "4. Division\n"
    "5. Programm Beenden\n")

# Liste mit zulässigen Eingaben für Errorhandling im Fall einer Falscheingabe durch Nutzer
    zulässige_eingabe = ["1","2","3","4","5"]
    # Errorhandling bei Falscheingabe
    if wahl not in zulässige_eingabe:
        print("Unzulässige Eingabe !"
              "Bitte nur Zahlen von 1 - 5 eingeben.")
        continue

    # Nutzer nach 2 Zahlen fragen
    zahl_1 = float(input("Zahl 1 eingeben:"))
    zahl_2 = float(input("Zahl 2 eingeben:"))

# conditional statements um bestimmte Rechenoperation
# basierend auf Nutzerauswahl durchzuführen
    if wahl == "1":
        addition(zahl_1, zahl_2)
    elif wahl == "2":
        subtraktion(zahl_1, zahl_2)
    elif wahl == "3":
        multiplikation(zahl_1, zahl_2)
    elif wahl == "4":
        division(zahl_1, zahl_2)
    elif wahl == "5":
        quit()
