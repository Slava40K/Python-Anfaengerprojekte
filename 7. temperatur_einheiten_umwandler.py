# Programm zur Umrechnung von Temperatur einheiten Celcius, Kelvin und Fahrenheit

# Definieren der Funktionen zur Umrechnung der Einheiten
def celsius_umwandeln(celsius):
    # Celsius zu F und K
    fahrenheit = (9/5 * celsius) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def fahrenheit_umwandeln(fahrenheit):
    # Fahrenheit zu C und K
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

def kelvin_umwandeln(kelvin):
    # Kelvin zu C und F
    celsius = kelvin - 273.15
    fahrenheit = (9/5 * celsius) + 32
    return celsius, fahrenheit

# HAUPTTEIL
# While Schleife um Nutzer Umwandlung wählen zu lassen

while True:
    print("\nWähle eine Umrechnung:")
    print("\n1. Celsius in Fahrenheit und Kelvin")
    print("2. Fahrenheit in Celsius und Kelvin")
    print("3. Kelvin in Celsius und Fahrenheit")
    print("4. Programm beenden")

    auswahl = input("\nEntsprechende Zahl eingeben und mit 'Enter' bestätigen: ")
    
    if auswahl == "1":
        celcius = float(input("\nTemperatur in Celsius ° eingeben: \n"))
        fahrenheit, kelvin = celsius_umwandeln(celcius)
        print(f"\nDie Temperatur beträgt {celcius}°C Celcius, {fahrenheit}°F Fahrenheit und {kelvin}K Kelvin.\n")
    
    elif auswahl == "2":
        fahrenheit = float(input("\nTemperatur in Fahrenheit° eingeben: \n"))
        celsius, kelvin = fahrenheit_umwandeln(fahrenheit)
        print(f"\nDie Temperatur beträgt {fahrenheit}°F Fahrenheit, {celsius}°C Celcius und {kelvin}K Kelvin.\n")
    
    elif auswahl == "3":
        kelvin = float(input("\nTemperatur in Kelvin° eingeben: \n"))
        celsius, fahrenheit = kelvin_umwandeln(kelvin)
        print(f"\nDie Temperatur beträgt {kelvin}K Kelvin, {celsius}°C Celcius und {fahrenheit}°F Fahrenheit.\n")
    
    elif auswahl == "4":
        print("\nProgramm beendet.\n")
        break
    else:
        print("\nUngültige Auswahl! Bitte eine Zahl zwischen 1 und 4 eingeben.\n")
