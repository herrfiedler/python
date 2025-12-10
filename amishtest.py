# Amish Test - Wie gut passt du in eine Amish Community? (15 Fragen)
# Autor: Herr Fiedler
# Lizenz: MIT License
# Diese Datei darf frei genutzt, verändert und weitergegeben werden.
# Vollständiger Lizenztext: https://opensource.org/licenses/MIT

def ask_question(question, options):
    """
    Stellt eine Frage mit Antwortmöglichkeiten und gibt die entsprechende Punktzahl zurück.
    options = [(antworttext, punktzahl), ...]
    """
    print("\n" + question)
    for i, (text, _) in enumerate(options, 1):
        print(f"{i}. {text}")

    while True:
        choice = input("Deine Antwort (Zahl eingeben): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1][1], options[int(choice) - 1][0]
        else:
            print("Bitte eine gültige Zahl eingeben.")


def main():
    print("Willkommen zum Amish-Kompatibilitäts-Test!")
    print("Dieser Test nutzt gewichtete Fragen und liefert ein differenziertes Ergebnis.\n")

    # Jede Frage: (Frage, Antworten, Gewicht, Bedeutung)
    questions = [
        # Sehr hohe Gewichtung
        ("Wie stark bist du bereit, moderne Technologie einzuschränken?",
         [("Ich könnte fast vollständig darauf verzichten", 10),
          ("Teilweise, aber mit Einschränkungen", 6),
          ("Nur ungern", 3),
          ("Gar nicht", 0)],
         3,
         "Technologieverzicht ist eine zentrale Grundlage des Amish-Lebens."),

        ("Wie zentral ist Religion in deinem Leben?",
         [("Sehr zentral", 10), ("Wichtig", 7), ("Etwas wichtig", 4), ("Kaum wichtig", 1)],
         3,
         "Religion strukturiert den gesamten Alltag und die Gemeinschaft."),

        ("Wie wichtig ist dir Gemeinschaft und gegenseitige Unterstützung?",
         [("Sehr wichtig", 10), ("Wichtig", 7), ("Geht so", 4), ("Weniger wichtig", 1)],
         3,
         "Die Amish leben in eng vernetzten Dorfgemeinschaften mit starker gegenseitiger Hilfe."),

        ("Wie gut kommst du mit klaren religiösen Regeln und Traditionen zurecht?",
         [("Sehr gut", 10), ("Ganz gut", 7), ("Eher schwer", 3), ("Gar nicht", 0)],
         3,
         "Die Ordnung (Ordnung) regelt nahezu alle Lebensbereiche."),

        # Mittlere Gewichtung
        ("Wie stehst du zu schlichter Kleidung und einfachen Lebensstilen?",
         [("Finde ich gut", 10), ("Ich könnte mich daran gewöhnen", 6),
          ("Fällt mir schwer", 3), ("Mag ich nicht", 0)],
         2,
         "Schlichte Kleidung symbolisiert Demut und Gleichheit."),

        ("Wie wichtig ist dir Konsum (Mode, Marken, Gadgets)?",
         [("Unwichtig", 10), ("Nicht sehr wichtig", 7), ("Mittel", 4), ("Sehr wichtig", 0)],
         2,
         "Amish vermeiden Luxus und Konsumorientierung bewusst."),

        ("Könntest du ohne Auto leben?",
         [("Ja, problemlos", 10), ("Wahrscheinlich", 6), ("Eher nicht", 3), ("Nein", 0)],
         2,
         "Auto-Verzicht stärkt lokale Gemeinschaft und Bescheidenheit."),

        ("Wie stehst du zur traditionellen Rollenverteilung?",
         [("Akzeptiere ich", 10), ("Kann ich mir vorstellen", 6),
          ("Neutral", 4), ("Lehne ich ab", 1)],
         2,
         "Die Familienstruktur der Amish ist klar traditionell geprägt."),

        ("Wie leicht fällt es dir, Konflikte ohne Streit oder Gewalt zu lösen?",
         [("Sehr leicht", 10), ("Meistens", 7), ("Schwierig", 3), ("Eher nein", 1)],
         2,
         "Amish praktizieren Gewaltfreiheit und Harmonieorientierung."),

        # Niedrige Gewichtung
        ("Wie wichtig ist dir ein entschleunigtes Leben?",
         [("Sehr wichtig", 10), ("Wichtig", 7), ("Neutral", 5), ("Nicht wichtig", 2)],
         1,
         "Amish leben bewusst langsam und ohne hektische Ablenkungen."),

        ("Wie sehr magst du Natur, Landwirtschaft oder Handwerk?",
         [("Sehr", 10), ("Ziemlich", 7), ("Geht so", 4), ("Gar nicht", 1)],
         1,
         "Viele Amish-Berufe sind handwerklich oder landwirtschaftlich."),

        ("Wie gut kannst du dich Autoritäten und Regeln unterordnen?",
         [("Sehr gut", 10), ("Ganz gut", 7), ("Schwierig", 3), ("Sehr schwierig", 1)],
         1,
         "Autorität und Regelbefolgung spielen im Gemeindeleben eine große Rolle."),

        ("Wie sehr liebst du körperliche Arbeit?",
         [("Sehr", 10), ("Ziemlich", 7), ("Solala", 4), ("Gar nicht", 1)],
         1,
         "Viele Tätigkeiten sind körperlich anspruchsvoll."),

        ("Wie wichtig ist dir Individualität im Vergleich zur Gemeinschaft?",
         [("Gemeinschaft ist wichtiger", 10),
          ("Beides ausgewogen", 6),
          ("Individualität ist wichtiger", 2)],
         1,
         "Amish betonen Gemeinschaft über Individualismus."),

        ("Wie gut kannst du ohne Internet leben?",
         [("Wochenlang", 10), ("Einige Tage", 6), ("Kaum", 3), ("Gar nicht", 0)],
         1,
         "Internet wird weitgehend gemieden."),

    ]

    total_score = 0
    max_score = 0
    answer_details = []  # speichert: (score_prozent, bedeutung, user_answer)

    for q, opts, weight, meaning in questions:
        score, answer_text = ask_question(q, opts)
        weighted_score = score * weight
        total_score += weighted_score
        max_score += 10 * weight

        # Für differenziertes Feedback
        relative = score / 10  # 1.0 = perfekt, 0 = gar nicht
        answer_details.append((relative, meaning, answer_text))

    percentage = round((total_score / max_score) * 100)

    # Sortiert: beste Antworten oben, schlechteste unten
    answer_details.sort(key=lambda x: x[0], reverse=True)

    print("\n--- Ergebnis ---")
    print(f"Kompatibilität mit einer Amish-Community: {percentage}%\n")

    # Kommentar Gesamt
    if percentage >= 85:
        comment = "Du würdest sehr gut in eine Amish-Community passen."
    elif percentage >= 70:
        comment = "Du würdest teilweise gut hineinpassen, aber manche Bereiche wären herausfordernd."
    elif percentage >= 50:
        comment = "Einige Aspekte passen zu dir, aber vieles wäre schwierig für dich."
    else:
        comment = "Das Amish-Leben unterscheidet sich stark von deinen Lebensgewohnheiten."

    print(comment)
    print("\n")

    # TOP 3 Stärken
    print("Bereiche, die besonders gut passen:")
    for rel, meaning, answer in answer_details[:3]:
        print(f"- {meaning} → Deine Antwort: '{answer}'")

    print("\nBereiche, die weniger gut passen:")
    for rel, meaning, answer in answer_details[-3:]:
        print(f"- {meaning} → Deine Antwort: '{answer}'")

    print("\nDanke fürs Mitmachen!")


if __name__ == "__main__":
    main()
