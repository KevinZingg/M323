import itertools
import random

def count_from_one():
    return itertools.count(1)

def generate_twos():
    return (x * 2 for x in itertools.count(1))

def generate_powers_of_two():
    return (2 ** x for x in itertools.count(1))

def generate_letters():
    def next_letter(sequence):
        while True:
            for letter in sequence:
                yield letter
            sequence = [f"{x}{y}" for x in sequence for y in "abcdefghijklmnopqrstuvwxyz"]
    return next_letter("abcdefghijklmnopqrstuvwxyz")

def roll_dice():
    while True:
        yield random.randint(1, 6)

# Example usage
if __name__ == "__main__":
    one_counter = count_from_one()
    print([next(one_counter) for _ in range(10)])

    twos_stream = generate_twos()
    print([next(twos_stream) for _ in range(10)])

    powers_of_two_stream = generate_powers_of_two()
    print([next(powers_of_two_stream) for _ in range(10)])

    letters_stream = generate_letters()
    print([next(letters_stream) for _ in range(52)])

    dice_stream = roll_dice()
    print([next(dice_stream) for _ in range(10)])
