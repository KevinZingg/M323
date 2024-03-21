# Übung 1
quadriert = [x**2 for x in range(1, 11)]
print(f"Debug: Übung 1 Quadrierte Zahlen = {quadriert}")

# Übung 2
gerade_zahlen = [x for x in range(1, 21) if x % 2 == 0]
print(f"Debug: Übung 2 Gerade Zahlen = {gerade_zahlen}")

# Übung 3
colors = ["Red", "Green", "Blue"]
fruits = ["Apple", "Banana", "Orange"]
farbe_frucht_paare = [(color, fruit) for color in colors for fruit in fruits]
print(f"Debug: Übung 3 Farbe-Frucht-Paare = {farbe_frucht_paare}")

# Übung 4
class User:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

users = [
    User("Alice", ["Task 1", "Task 2", "Task 3"]),
    User("Bob", ["Task 1", "Task 4", "Task 5"]),
    User("Charlie", ["Task 2", "Task 3", "Task 6"])
]

tasksCompleted = ["Task 1", "Task 3", "Task 5"]

pending_tasks = [(user.name, task) for user in users for task in user.tasks if task not in tasksCompleted]
print(f"Debug: Übung 4 Ausstehende Aufgaben = {pending_tasks}")
