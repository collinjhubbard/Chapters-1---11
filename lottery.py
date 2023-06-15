import random

lottery = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 'a', 's', 'd', 'f', 'g']

winning_number = random.sample(lottery, 4)
print(f"If you have a ticket matching these numbers {winning_number} then you've won!")
