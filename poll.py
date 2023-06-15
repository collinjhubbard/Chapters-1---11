responses = {}

polling_active = True

while polling_active:
    name = input(f"\nWhat is your name? ")
    response = input(f"Who is your favored candidate right now? ")

    responses[name] = response

    repeat = input(f"Would someone else like to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} favors {response} for president")