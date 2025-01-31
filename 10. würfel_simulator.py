# Würfeln: Ein Programm bauen, das das Würfeln von Würfeln simuliert.
# Ermögliche dem Benutzer, die Anzahl der Würfel und Seiten festzulegen,
# und zeige die Ergebnisse an.

# Importiere das Modul für zufällige Würfelergebnisse
import random

# Funktion für einen einzelnen Würfelwurf
def wuerfeln_einmal(wuerfelseiten):
    ergebnis = random.randint(1, wuerfelseiten)
    print(f"Du hast eine {ergebnis} geworfen.\n")
    return ergebnis

# Funktion für mehrere Würfe
def mehrere_wuerfe(wuerfelanzahl, wuerfelseiten):
    for _ in range(wuerfelanzahl):
        wuerfeln_einmal(wuerfelseiten)

# Benutzereingabe, um die Anzahl der Seiten und Würfel festzulegen
while True:
    try:
        wuerfelanzahl = int(input("Wie viele Würfel möchtest du werfen?\n"))
        wuerfelseiten = int(input("Wie viele Seiten soll der Würfel haben?\n"))
        break
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

# if-Anweisungen
if wuerfelanzahl == 1:
    wuerfeln_einmal(wuerfelseiten)
else:
    mehrere_wuerfe(wuerfelanzahl, wuerfelseiten)
