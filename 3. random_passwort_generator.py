# Programm zum Generieren von zufälligen Passwörtern
# mit einer Länge von 8-12 Zeichen und Nutzung von Groß- und Kleinbuchstaben, Sonderzeichen und Zahlen

import random
# Liste mit allen Buchstaben, Zeichen und Zahlen die für das Passwort genutzt werden
zeichen_liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         '!', '#', '$', '%', '&', '(', ')', '*', '+']

# leere Liste um Zeichen zu speichern und später zu einem Passwort-String zusammenzufügen
stringliste = []

# zufällige Festlegung einer Passwortlänge von 8-12
pw_länge = random.randint(8,12)

# for Schleife um zufällige Zahlen zu generieren, die dann mit Index platz der Zeichen
# in der Zeichenliste abgeglichen werden und der stringliste zugefügt werden.
for digits in range(pw_länge):
    
    i = random.randint(1,len(zeichen_liste))
    random.shuffle(zeichen_liste) # 'mischen' der zeichenliste um höhere Zufälligkeit zu erreichen
    
    if i < len(zeichen_liste):
        char = zeichen_liste[i]
        stringliste.append(char)
    
    elif i == len(zeichen_liste):
        char = zeichen_liste[i-1]
        stringliste.append(char)

# alle zeichen in der stringliste werden nun zu einem String zusammengefügt 
# und dieser wird in der Variable password gespeichert.
password = "".join(stringliste)

# print call mit f-strings um finale Nachricht mit dem Passwort anzuzeigen
print(  f"\nDein zufällig generiertes Passwort lautet: {password}"
        f" , ist {pw_länge} Zeichen lang und beinhaltet Klein/Großbuchstaben, Sonderzeichen und Zahlen\n")

