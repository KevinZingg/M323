persons = [("Joe", 25), ("Max", 16), ("Joe", 12), ("Kirstin", 20)]

for name, age in persons:
    if name == "Joe" or age > 18:
        print(f"Match found: {name}")
