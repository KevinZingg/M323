greetings = {"Hello", "Hi there"}
names = {"Alice", "Bob"}

combinations = {f"{greeting}, {name}!" for greeting in greetings for name in names}

print("Combinations:", combinations)
