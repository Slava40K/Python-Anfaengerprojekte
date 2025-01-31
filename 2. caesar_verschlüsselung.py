# Programm zur Verschlüsselung und Entschlüsselung von Nachrichten,
# das, die 'Cäsar'-Verschlüsselungsmethode nutzt

# Alphabet mit den Buchstaben von a bis z
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 'caesar' Funktion zum Verschlüsseln und Entschlüsseln
def caesar(richtung, text, verschiebung):
    
    # Verschlüsselung, wenn die Richtung '1' ist
    if richtung == '1':
        verschluesselte_zeichen_string = ""  # Variable für die verschlüsselte Nachricht
        # Für jedes Zeichen im Text
        for zeichen in text:
            if zeichen in alphabet:  # Überprüfe, ob das Zeichen im Alphabet enthalten ist
                verschluesselt_zeichen = alphabet.index(zeichen) + verschiebung  # Verschiebe das Zeichen um 'verschiebung'
                verschluesselt_zeichen %= len(alphabet)  # Verhindert einen Indexfehler, falls die Verschiebung das Alphabet übersteigt
                verschluesselte_zeichen_string += alphabet[verschluesselt_zeichen]  # Füge das verschlüsselte Zeichen zur Ausgabe hinzu
            else:
                verschluesselte_zeichen_string += zeichen  # Füge nicht-alphabetische Zeichen unverändert hinzu
        print(verschluesselte_zeichen_string)  # Gib die verschlüsselte Nachricht aus

    # Entschlüsselung, wenn die Richtung '2' ist
    if richtung == '2':
        entschluesselte_zeichen_string = ""  # Variable für die entschlüsselte Nachricht
        # Für jedes Zeichen im Text
        for zeichen in text:
            if zeichen in alphabet:  # Überprüfe, ob das Zeichen im Alphabet enthalten ist
                entschluesselt_zeichen = alphabet.index(zeichen) - verschiebung  # Verschiebe das Zeichen rückwärts um 'verschiebung'
                entschluesselt_zeichen %= len(alphabet)  # Verhindert einen Indexfehler, falls die Verschiebung das Alphabet übersteigt
                entschluesselte_zeichen_string += alphabet[entschluesselt_zeichen]  # Füge das entschlüsselte Zeichen zur Ausgabe hinzu
            else:
                entschluesselte_zeichen_string += zeichen  # Füge nicht-alphabetische Zeichen unverändert hinzu
        print(entschluesselte_zeichen_string)  # Gib die entschlüsselte Nachricht aus

# while Schleife, um dem Benutzer zu ermöglichen, das Programm weiter zu verwenden oder zu beenden.
while True:
    # Benutzer nach der Richtung fragen (Verschlüsselung oder Entschlüsselung)
    richtung = input("Gib '1' ein, um zu verschlüsseln, gib '2' ein, um zu entschlüsseln:\n")
    # Benutzer nach dem Text fragen, der verschlüsselt oder entschlüsselt werden soll
    text = input("Gib deine Nachricht ein:\n").lower()  # Der Text wird in Kleinbuchstaben umgewandelt
    # Benutzer nach der Verschiebungszahl fragen
    verschiebung = int(input("Gib die Verschiebungszahl ein:\n"))
    
    # Aufruf der Caesar-Funktion mit den angegebenen Parametern
    caesar(richtung, text, verschiebung)
    
    # Benutzer fragen, ob er eine weitere Verschlüsselung/Entschlüsselung durchführen möchte
    nochmal = input("Möchtest du es nochmal versuchen? Gib: 'J' für Ja und 'N' für Nein: ").lower()
    if nochmal == 'J':
        continue  # Wenn der Benutzer mit 'J' antwortet, wird der Prozess wiederholt
    elif nochmal == 'N':
        print("Programm wird beendet.")  # Bei 'N' wird das Programm beendet
        break
