# Übung 1
listen_von_zahlen = [[1, 2], [3, 4], [5, 6]]
verdoppelt = [x * 2 for sublist in listen_von_zahlen for x in sublist]
print(f"Debug: Übung 1 Verdoppelte Zahlen = {verdoppelt}")

# Übung 2
personen_farben = [("Max", ["Blau", "Grün"]), ("Anna", ["Rot"]), ("Julia", ["Gelb", "Blau", "Grün"])]
einzigartige_farben = list(set(farbe for _, farben in personen_farben for farbe in farben))
print(f"Debug: Übung 2 Einzigartige Farben = {einzigartige_farben}")
