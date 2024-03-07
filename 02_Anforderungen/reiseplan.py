destinations = []

def add_destination(destination):
    destinations.append(destination)
    print(f"Debug: Added destination {destination}")

def insert_destination_after(destination_to_insert, after_destination):
    try:
        index = destinations.index(after_destination)
        destinations.insert(index + 1, destination_to_insert)
        print(f"Debug: Inserted {destination_to_insert} after {after_destination}")
    except ValueError:
        add_destination(destination_to_insert)

def modify_route(old_destination, new_destination):
    try:
        index = destinations.index(old_destination)
        destinations[index] = new_destination
        print(f"Debug: Modified route from {old_destination} to {new_destination}")
    except ValueError:
        print(f"Debug: {old_destination} not in destinations list")

# Beispiele für die Nutzung
add_destination("Paris")
insert_destination_after("Köln", "Paris")
modify_route("Paris", "Berlin")
