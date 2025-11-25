# Nautischer Rechner
# Autor: Herr Fiedler
# Lizenz: MIT License
# Diese Datei darf frei genutzt, verändert und weitergegeben werden.
# Vollständiger Lizenztext: https://opensource.org/licenses/MIT


def nautischer_rechner():
    print(" ")
    print("="*63)
    print("============> Willkommen zum nautischen Rechner! <=============")
    print("="*63)
    print("\nEinfach Geschwindigkeiten, Entfernungen und die Fahrtdauer von Booten berechnen!\n")
    print("Was möchtest du berechnen? Wähle:\n")
    print("(1) Geschwindigkeit")
    print("(2) Entfernung")
    print("(3) Fahrtdauer\n")

    programmwahl = input("Deine Auswahl: ").strip()

    if programmwahl == "1":
        print(f"Du hast Programm ({programmwahl}) Geschwindigkeit gewählt.")
        distanz = float(input("\nWie groß ist die Distanz in Seemeilen? "))
        zeit = float(input("Wieviele Minuten fährt das Schiff? "))

        geschwindigkeit = distanz * 60 / zeit
        kmh = geschwindigkeit * 1.852
        km = distanz * 1.852

        print("\n=======> Deine Reisedaten wurden wie folgt berechnet: <========")
        print(f"Geschwindigkeit: {geschwindigkeit:.2f} Knoten (= {kmh:.2f} km/h)")
        print(f"Distanz: {distanz:.2f} Seemeilen (= {km:.2f} km)")
        print(f"Fahrtdauer: {zeit:.2f} Minuten")

    elif programmwahl == "2":
        print(f"Du hast Programm ({programmwahl}) Distanz gewählt.")
        geschwindigkeit = float(input("\nWie groß ist die Geschwindigkeit in Knoten? "))
        zeit = float(input("Wieviele Minuten fährt das Schiff? "))

        distanz = geschwindigkeit * zeit / 60
        kmh = geschwindigkeit * 1.852
        km = distanz * 1.852

        print("\n=======> Deine Reisedaten wurden wie folgt berechnet: <========")
        print(f"Geschwindigkeit: {geschwindigkeit:.2f} Knoten (= {kmh:.2f} km/h)")
        print(f"Distanz: {distanz:.2f} Seemeilen (= {km:.2f} km)")
        print(f"Fahrtdauer: {zeit:.2f} Minuten")

    elif programmwahl == "3":
        print(f"Du hast Programm ({programmwahl}) Fahrtdauer gewählt.")
        geschwindigkeit = float(input("\nWie groß ist die Geschwindigkeit in Knoten? "))
        distanz = float(input("Wie groß ist die Distanz in Seemeilen? "))

        zeit = distanz * 60 / geschwindigkeit
        kmh = geschwindigkeit * 1.852
        km = distanz * 1.852

        print("\n=======> Deine Reisedaten wurden wie folgt berechnet: <========")
        print(f"Geschwindigkeit: {geschwindigkeit:.2f} Knoten (= {kmh:.2f} km/h)")
        print(f"Distanz: {distanz:.2f} Seemeilen (= {km:.2f} km)")
        print(f"Fahrtdauer: {zeit:.2f} Minuten")

    else:
        print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")

    print("\n" + "="*63)
    print("Mast und Schotbruch und immer eine Hand Wasser unter dem Kiel!")
    print("="*63 + "\n")


# Programm starten
if __name__ == "__main__":
    nautischer_rechner()
