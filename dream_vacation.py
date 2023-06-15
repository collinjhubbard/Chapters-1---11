dream_vacation = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could go one place in the world, where would you go? ")

    dream_vacation[name] = response

    repeat = input("Would you like someone else to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n --- Poll Results ---")
for name, response in dream_vacation.items():
    print(f"If {name} could go one place in the world, they would go to {response}.")
