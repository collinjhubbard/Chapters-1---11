from random import randint

class Die:
    
    def __init__(self, sides=6):
        self.sides = sides

    def describe_die(self):
        print(f"this die has {self.sides} sides")

    def roll_die(self):
        rolling = randint(1, self.sides)
        return rolling


my_die = Die(20)
print(my_die.roll_die())
my_die.describe_die()