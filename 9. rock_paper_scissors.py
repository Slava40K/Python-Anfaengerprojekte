# Ein simples Schere Stein Papier Spiel, bei dem der Nutzer gegen
# den Computer spielen kann

# random Modul für die CPU-Wahl importieren
import random

# counter-variablen für Siege/Niederlagen/Unentschieden
Siege = 0
Niederlagen = 0
Unentschieden = 0

# Liste der möglichen Gesten
cpu_gesten = ["Schere", "Stein", "Papier"]

# Funktion, die das Spiel für jede Wahl überprüft
def spiele_runde(nutzer_wahl):
    global Siege, Niederlagen, Unentschieden
    
    cpu_wahl = random.choice(cpu_gesten)
    print(f"Ihr Gegner wählt: {cpu_wahl}.")
    
    if nutzer_wahl == cpu_wahl:
        print("Unentschieden!\n")
        Unentschieden += 1
    elif (nutzer_wahl == "Schere" and cpu_wahl == "Papier") or \
         (nutzer_wahl == "Stein" and cpu_wahl == "Schere") or \
         (nutzer_wahl == "Papier" and cpu_wahl == "Stein"):
        print("Sie haben gewonnen!\n")
        Siege += 1
    else:
        print("Sie haben verloren.\n")
        Niederlagen += 1

# while-Schleife, um Nutzerwahl zu ermöglichen
while True:

    nutzer_wahl = input("Bitte wählen Sie:\n"
                        "1. Schere\n"
                        "2. Stein\n"
                        "3. Papier\n"
                        "4. Programm beenden\n")

    # Beenden des Programms
    if nutzer_wahl == "4":
        print("Programm wird beendet.")
        break

    # Validierung der Eingabe
    if nutzer_wahl == "1":
        print("Sie wählen Schere.")
        spiele_runde("Schere")
    elif nutzer_wahl == "2":
        print("Sie wählen Stein.")
        spiele_runde("Stein")
    elif nutzer_wahl == "3":
        print("Sie wählen Papier.")
        spiele_runde("Papier")
    else:
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2, 3 oder 4.\n")
        continue

    # Siege/Niederlagen/Unentschieden anzeigen
    print(f"Siege: {Siege}\nNiederlagen: {Niederlagen}\nUnentschieden: {Unentschieden}\n")
