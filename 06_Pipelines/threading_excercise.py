import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random


inventory = {'smartphones': 10}
lock = threading.Lock()

def add_to_cart(items_to_add):
    global inventory
    item_name = 'smartphones'

    # Simuliert reading inventory und processing time
    time.sleep(random.uniform(0.1, 0.5))
    with lock:
        print(f"Debug: Checking inventory for {item_name}. Current stock: {inventory[item_name]}")
        if inventory[item_name] >= items_to_add:
            inventory[item_name] -= items_to_add
            print(f"Debug: Added {items_to_add} {item_name} to cart. New stock: {inventory[item_name]}")
        else:
            print(f"Debug: Not enough {item_name} in stock to add {items_to_add} to cart.")

def simulate_shopping():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(10):
            executor.submit(add_to_cart, 1)

if __name__ == "__main__":
    simulate_shopping()
    print(f"Final inventory: {inventory}")
