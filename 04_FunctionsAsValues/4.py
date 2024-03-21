from functools import reduce

# Übung 1
zahle = [1, 2, 3, 4, 5]
summe = reduce(lambda acc, n: acc + n, zahle, 0)
print(f"Debug: Übung 1 Summe = {summe}")

# Übung 2
strings = ["Hallo", " ", "Welt", "!"]
kombiniert = reduce(lambda acc, s: acc + s, strings, "")
print(f"Debug: Übung 2 Kombinierte Strings = {kombiniert}")

# Übung 3
punkte = [(1, 3), (2, 5), (4, 8), (6, 2)]
schwerpunkt_sum = reduce(lambda acc, p: (acc[0] + p[0], acc[1] + p[1]), punkte, (0, 0))
anzahl_punkte = len(punkte)
schwerpunkt = (schwerpunkt_sum[0] / anzahl_punkte, schwerpunkt_sum[1] / anzahl_punkte)
print(f"Debug: Übung 3 Schwerpunkt = {schwerpunkt}")
