# Übung 1
zahle = [1, 2, 3, 4, 5]
verdoppelt = list(map(lambda x: x * 2, zahle))
print("Debug: Übung 1 Ergebnis:", verdoppelt)

# Übung 2
namen = ["Alice", "Bob", "Charlie"]
grossbuchstaben = list(map(lambda x: x.upper(), namen))
print("Debug: Übung 2 Ergebnis:", grossbuchstaben)

# Übung 3
zahle = [12, 45, 68, 100]
halbiert = list(map(lambda x: x / 2, zahle))
print("Debug: Übung 3 Ergebnis:", halbiert)

# Übung 4
class Adresse:
    def __init__(self, strasse, hausnummer, postleitzahl, stadt):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.postleitzahl = postleitzahl
        self.stadt = stadt

adressen = [
    Adresse("Hauptstrasse", 10, "12345", "Musterstadt"),
    Adresse("Nebenstrasse", 5, "23456", "Beispielburg")
]

formatierte_adressen = list(map(lambda a: f"{a.strasse} {a.hausnummer}, {a.postleitzahl} {a.stadt}", adressen))
print("Debug: Übung 4 Ergebnis:", formatierte_adressen)

# Übung 5
namen = ["Max Mustermann", "Erika Mustermann"]
vornamen_gross = list(map(lambda x: x.split()[0].upper(), namen))
print("Debug: Übung 5 Ergebnis:", vornamen_gross)
