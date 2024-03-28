import random

class IO:
    def __init__(self, operation):
        self.operation = operation

    def map(self, func):
        return IO(lambda: func(self.operation()))

    def flatMap(self, func):
        return IO(lambda: func(self.operation()).operation())

    def unsafeRunSync(self):
        return self.operation()

# Impure function
def rollDiceImpure():
    return random.randint(1, 6)

# Pure function encapsulating an impure operation
def rollDice():
    return IO(lambda: rollDiceImpure())

def allowToLeaveHome():
    return rollDice().map(lambda result: result == 6)

# Main logic
if __name__ == "__main__":
    # This line remains pure
    allow_to_leave = allowToLeaveHome()

    # Only becomes impure when explicitly run
    result = allow_to_leave.unsafeRunSync()
    print(f"Allowed to leave home: {result}")
