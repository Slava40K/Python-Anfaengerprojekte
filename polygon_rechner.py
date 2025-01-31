import math

# Basisklasse für polygonale Formen
class Polygone:
    def __init__(self, länge_a, breite):
        self.länge_a, self.breite = länge_a, breite

    # Berechnung des Umfangs eines Rechtecks
    def umfang_rechteck(self):
        return 2 * (self.länge_a + self.breite)
    
    # Berechnung der Fläche eines Rechtecks
    def fläche_rechteck(self):
        return self.länge_a * self.breite
    
    # Berechnung des Umfangs eines Quadrats
    def umfang_quadrat(self):
        return self.länge_a * 4
    
    # Berechnung der Fläche eines Quadrats
    def fläche_quadrat(self):
        return self.länge_a ** 2

# Klasse für Dreiecke
class Dreieck:
    def __init__(self, länge_a, länge_b, länge_c):
        self.länge_a, self.länge_b, self.länge_c = länge_a, länge_b, länge_c

    # Berechnung des Umfangs eines Dreiecks
    def umfang_dreieck(self):
        return self.länge_a + self.länge_b + self.länge_c
    
    # Berechnung der Fläche eines Dreiecks 
    def fläche_dreieck(self):
        s = self.umfang_dreieck() / 2
        return math.sqrt(s * (s - self.länge_a) * (s - self.länge_b) * (s - self.länge_c))

# Klasse für Trapeze
class Trapez:
    def __init__(self, höhe, länge_a, länge_b, länge_c, länge_d):
        self.höhe, self.länge_a, self.länge_b, self.länge_c, self.länge_d = höhe, länge_a, länge_b, länge_c, länge_d

    # Berechnung des Umfangs eines Trapezes
    def umfang_trapez(self):
        return self.länge_a + self.länge_b + self.länge_c + self.länge_d
    
    # Berechnung der Fläche eines Trapezes
    def fläche_trapez(self):
        return (self.höhe / 2) * (self.länge_a + self.länge_b)

# Klasse für Rechtecke, erbt von Polygone
class Rechteck(Polygone):
    pass

# Klasse für Quadrate, erbt von Polygone
class Quadrat(Polygone):
    def __init__(self, länge_a):
        super().__init__(länge_a, länge_a)

# Hauptprogramm mit einer while schleife Benutzereingaben
while True:
    figur_wahl = input("Wählen Sie eine der Figuren:\n1. Rechteck\n2. Quadrat\n3. Dreieck\n4. Trapez\n5. Programm beenden.\n")
    if figur_wahl == "5":
        print("Programm wird beendet.")
        break
    
    try:
        werte = []
        # Je nach Wahl des Nutzers passende Werte einlesen
        if figur_wahl == "1":
            werte.append(int(input("Bitte Länge in cm eingeben:\n")))
            werte.append(int(input("Bitte Breite in cm eingeben:\n")))
        elif figur_wahl == "2":
            werte.append(int(input("Bitte Länge in cm eingeben:\n")))
        elif figur_wahl == "3":
            werte.append(int(input("Bitte Seitenlänge A in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge B in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge C in cm eingeben:\n")))
        elif figur_wahl == "4":
            werte.append(int(input("Bitte Höhe in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge A in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge B in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge C in cm eingeben:\n")))
            werte.append(int(input("Bitte Seitenlänge D in cm eingeben:\n")))
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            continue
        
        # Erzeugung der gewählten Figur und Berechnung der Werte
        if figur_wahl == "1":
            figur = Rechteck(*werte)
            print(f"Der Umfang beträgt: {figur.umfang_rechteck()} cm.")
            print(f"Die Fläche beträgt: {figur.fläche_rechteck()} cm².")
        elif figur_wahl == "2":
            figur = Quadrat(*werte)
            print(f"Der Umfang beträgt: {figur.umfang_quadrat()} cm.")
            print(f"Die Fläche beträgt: {figur.fläche_quadrat()} cm².")
        elif figur_wahl == "3":
            figur = Dreieck(*werte)
            print(f"Der Umfang beträgt: {figur.umfang_dreieck()} cm.")
            print(f"Die Fläche beträgt: {figur.fläche_dreieck():.2f} cm².")
        elif figur_wahl == "4":
            figur = Trapez(*werte)
            print(f"Der Umfang beträgt: {figur.umfang_trapez()} cm.")
            print(f"Die Fläche beträgt: {figur.fläche_trapez():.2f} cm².")
    except ValueError:
        print("Fehlerhafte Eingabe. Bitte geben Sie nur ganze Zahlen ein.")
