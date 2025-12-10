# Börsenspiel
# Autor: Herr Fiedler & KI
# Lizenz: MIT License
# Diese Datei darf frei genutzt, verändert und weitergegeben werden.
# Vollständiger Lizenztext: https://opensource.org/licenses/MIT


import random  # Zufallsgenerator importieren, um Kursänderungen zu simulieren

# -----------------------------
# Klasse für eine Aktie
# -----------------------------
class Aktie:
    def __init__(self, name, kurs):
        self.name = name                # Name der Aktie
        self.kurs = kurs                # Aktueller Kurs der Aktie

    def kurs_aendern(self):
        """Ändert den Kurs zufällig um -10% bis +10%"""
        aenderung = random.uniform(-0.10, 0.10)  # Zufällige Änderung berechnen
        self.kurs += self.kurs * aenderung       # Kurs aktualisieren
        if self.kurs < 1:
            self.kurs = 1                        # Mindestkurs auf 1 EUR setzen

# -----------------------------
# Hauptprogramm
# -----------------------------
def main():
    geld = 10000                  # Startkapital des Spielers
    depot = {}                    # Dictionary für Aktienbesitz: {Aktienname: Anzahl}

    # Liste der verfügbaren Aktien
    aktien = [
        Aktie("Apple", 180),      # Aktie Apple mit Startkurs 180 EUR
        Aktie("Tesla", 220),      # Aktie Tesla
        Aktie("Microsoft", 320),  # Aktie Microsoft
        Aktie("Amazon", 140),     # Aktie Amazon
    ]

    # Anfangsbesitz = 0 für alle Aktien
    for aktie in aktien:
        depot[aktie.name] = 0     # Setzt die Anzahl gekaufter Aktien auf 0

    print("Willkommen zum einfachen Börsenspiel!")  # Begrüßung
    print(f"Startkapital: {geld} EUR\n")            # Startkapital anzeigen

    spiel_laueft = True        # Spielstatus

    while spiel_laueft:
        # -----------------------------
        # Aktuelle Kurse und Depot anzeigen
        # -----------------------------
        print("\nAktuelle Kurse:")
        for i, aktie in enumerate(aktien):
            # Index, Name, Kurs und Besitz ausgeben
            print(f"{i}) {aktie.name} | Kurs: {aktie.kurs:.2f} EUR | Besitz: {depot[aktie.name]}")

        print(f"Geld verfügbar: {geld:.2f} EUR")   # Verfügbares Geld anzeigen
        print("Was möchtest du tun?")
        print("1) Aktie kaufen")
        print("2) Aktie verkaufen")
        print("3) Runde beenden (Kurse ändern sich)")
        print("4) Spiel beenden")

        auswahl = input("Auswahl (1-4): ")         # Benutzereingabe

        # -----------------------------
        # Option 1: Aktie kaufen
        # -----------------------------
        if auswahl == "1":
            index = int(input("Welche Aktie (Index)? "))  # Index der Aktie abfragen
            menge = int(input("Wie viele kaufen? "))      # Anzahl der Aktien abfragen
            kosten = menge * aktien[index].kurs          # Gesamtkosten berechnen

            if kosten > geld:
                print("Nicht genug Geld!")               # Prüfen, ob genug Geld vorhanden
            else:
                geld -= kosten                           # Geld abziehen
                depot[aktien[index].name] += menge       # Aktien im Depot erhöhen
                print(f"Gekauft: {menge}x {aktien[index].name}")  # Kauf ausgeben

        # -----------------------------
        # Option 2: Aktie verkaufen
        # -----------------------------
        elif auswahl == "2":
            index = int(input("Welche Aktie (Index)? "))  # Index der Aktie abfragen
            menge = int(input("Wie viele verkaufen? "))   # Anzahl der Aktien abfragen
            besitz = depot[aktien[index].name]            # Besitz im Depot prüfen

            if menge > besitz:
                print("Du besitzt nicht genug Aktien!")  # Prüfen, ob genügend Aktien vorhanden
            else:
                geld += menge * aktien[index].kurs        # Geld durch Verkauf erhalten
                depot[aktien[index].name] -= menge        # Aktienbestand reduzieren
                print(f"Verkauft: {menge}x {aktien[index].name}")  # Verkauf ausgeben

        # -----------------------------
        # Option 3: Runde beenden, Kurse ändern
        # -----------------------------
        elif auswahl == "3":
            print("Die Kurse ändern sich...")
            for aktie in aktien:
                aktie.kurs_aendern()                       # Zufällige Kursänderung

        # -----------------------------
        # Option 4: Spiel beenden
        # -----------------------------
        elif auswahl == "4":
            spiel_laueft = False                            # Spiel beenden

        # -----------------------------
        # Ungültige Eingabe
        # -----------------------------
        else:
            print("Ungültige Eingabe!")                    # Meldung bei falscher Eingabe

    # -----------------------------
    # Endabrechnung
    # -----------------------------
    depot_wert = sum(depot[aktie.name] * aktie.kurs for aktie in aktien)  # Wert des Depots berechnen
    print("\n=== Spielende ===")
    print(f"Restgeld: {geld:.2f} EUR")                      # Restgeld ausgeben
    print(f"Depotwert: {depot_wert:.2f} EUR")              # Depotwert ausgeben
    print(f"Gesamtvermögen: {geld + depot_wert:.2f} EUR")  # Gesamtvermögen ausgeben

# -----------------------------
# Programm starten
# -----------------------------
if __name__ == "__main__":
    main()
