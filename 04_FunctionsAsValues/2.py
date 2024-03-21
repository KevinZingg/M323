# Übung 1
zahle = [1, 2, 3, 4, 5]
gerade_zahle = list(filter(lambda x: x % 2 == 0, zahle))
print("Debug: Übung 1 Ergebnis:", gerade_zahle)

# Übung 2
namen = ["Alice", "Bob", "Charlie", "Diana"]
lange_namen = list(filter(lambda x: len(x) > 4, namen))
print("Debug: Übung 2 Ergebnis:", lange_namen)

# Übung 3
zahle = [12, 45, 68, 100]
grosser_als_50 = list(filter(lambda x: x > 50, zahle))
print("Debug: Übung 3 Ergebnis:", grosser_als_50)

# Übung 4
woerter = ["Scala", "ist", "fantastisch"]
beginnt_mit_s = list(filter(lambda x: x.startswith('S'), woerter))
print("Debug: Übung 4 Ergebnis:", beginnt_mit_s)

# Übung 5
class Buch:
    def __init__(self, titel, autor, jahr):
        self.titel = titel
        self.autor = autor
        self.jahr = jahr

buecher = [
    Buch("1984", "George Orwell", 1949),
    Buch("Brave New World", "Aldous Huxley", 1932),
    Buch("Fahrenheit 451", "Ray Bradbury", 1953)
]

vor_1950 = list(map(lambda b: b.titel, filter(lambda b: b.jahr < 1950, buecher)))
print("Debug: Übung 5 Ergebnis:", vor_1950)
