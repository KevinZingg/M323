# Übung 1
class Mitarbeiter:
    def __init__(self, name, abteilung, gehalt):
        self.name = name
        self.abteilung = abteilung
        self.gehalt = gehalt

mitarbeiter = [
    Mitarbeiter("Max Mustermann", "IT", 50000),
    Mitarbeiter("Erika Musterfrau", "Marketing", 45000),
    Mitarbeiter("Klaus Klein", "IT", 55000),
    Mitarbeiter("Julia Gross", "HR", 40000)
]

it_mitarbeiter_hohes_gehalt = list(map(lambda m: m.name.split()[0].upper(),
                                       filter(lambda m: m.abteilung == "IT" and m.gehalt > 50000, mitarbeiter)))
print("Debug: Übung 1 Ergebnis:", it_mitarbeiter_hohes_gehalt)

# Übung 2
kurse = [
    "Programmierung in Scala",
    "Datenbanken",
    "Webentwicklung mit JavaScript",
    "Algorithmen und Datenstrukturen"
]

kurse_mit_daten = list(filter(lambda k: "Daten" in k, kurse))
kurse_ohne_leerzeichen = list(map(lambda k: k.replace(" ", ""), kurse_mit_daten))
sortiert_alphabetisch = sorted(kurse_ohne_leerzeichen)
sortiert_umgekehrt_alphabetisch = sorted(kurse_ohne_leerzeichen, reverse=True)

print("Debug: Übung 2 Ergebnis, alphabetisch:", sortiert_alphabetisch)
print("Debug: Übung 2 Ergebnis, umgekehrt alphabetisch:", sortiert_umgekehrt_alphabetisch)
