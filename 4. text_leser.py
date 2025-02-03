# Einfaches Notepad-Programm, das den Inhalt einer .txt-Datei öffnen und anzeigen kann,
# sowie neue Informationen hinzuzufügen und zu speichern.

def oeffne_und_lese(datei_pfad):
    try:
        # Öffnet die Datei im Lese-Modus ("r") und gibt ihren Inhalt aus
        with open(datei_pfad, "r") as datei:  
            inhalt = datei.read()
            print("\n", inhalt, "\n")
    except FileNotFoundError:
        # Fehlerbehandlung, falls die Datei nicht gefunden wird
        print("Fehler: Die angegebene Datei wurde nicht gefunden. Bitte überprüfen Sie den Pfad.")
    except Exception as e:
        # Allgemeine Fehlerbehandlung für andere Fehler
        print(f"Ein Fehler ist aufgetreten: {e}")


def schreibe_und_speichere(datei_pfad):
    try:
        # Öffnet die Datei im Anhänge-Modus ("a") zum Schreiben
        with open(datei_pfad, "a") as datei:
            hinzugefügter_text = input(
                "Bitte geben Sie den Text ein, der in die Datei geschrieben werden soll:"
            )  # Benutzer gibt den Text ein, der gespeichert werden soll
            datei.write(hinzugefügter_text + "\n")  # Der Text wird in die Datei geschrieben
            print("Änderungen wurden gespeichert.")
    except FileNotFoundError:
        # Fehlerbehandlung, falls die Datei nicht gefunden wird
        print("Fehler: Die angegebene Datei wurde nicht gefunden. Bitte überprüfen Sie den Pfad.")
    except Exception as e:
        # Allgemeine Fehlerbehandlung für andere Fehler
        print(f"Ein Fehler ist aufgetreten: {e}")


# Hauptschleife, um den Benutzer wiederholt nach einer Aktion zu fragen
while True:
    # Menüoptionen anzeigen und Benutzer zur Auswahl auffordern
    auswahl = input(
        "\nWählen Sie eine Funktion:\n"
        "1. Text-Datei lesen\n"
        "2. In Text-Datei schreiben und speichern\n"
        "3. Programm beenden\n"
    )

    if auswahl == "3":
        # Beendet die Schleife und damit das Programm, wenn der Benutzer '3' wählt
        print("Programm wird beendet.")
        break

    # Eingabe des Dateipfads, den der Benutzer öffnen oder bearbeiten möchte
    datei_pfad = input(
        "Geben Sie den Pfad der Text-Datei ein, die geöffnet oder bearbeitet werden soll:\n"
        "Gehen Sie dazu mit Rechtsklick auf die zu öffnende .txt Datei und wählen Sie 'Pfad kopieren'. "
        "Fügen Sie den Pfad dann hier ein (STRG + V): "
    ).strip('""')  # Entfernt unnötige Anführungszeichen aus dem eingegebenen Pfad

    # Abhängig von der Benutzerwahl wird entweder die Lese- oder Schreibfunktion aufgerufen
    if auswahl == "1":
        oeffne_und_lese(datei_pfad)
    elif auswahl == "2":
        schreibe_und_speichere(datei_pfad)
    else:
        # Wenn der Benutzer eine ungültige Auswahl trifft, wird eine Fehlermeldung angezeigt
        print("Ungültige Auswahl. Bitte wählen Sie eine der angegebenen Optionen.")
