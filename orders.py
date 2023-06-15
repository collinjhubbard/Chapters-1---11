sandwich_orders = ['Italian Beef','pastrami', 'The Northsider', 'pastrami','The Uptown Special', 'Classic Rueben', 'pastrami']
finished_sandwiches = []
print(f"What can we get started for you today? I should let you know that we are all out of pastrami. ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Your {sandwich} is being made right now")
    finished_sandwiches.append(sandwich)

print(f"\nThe following orders are ready: ")
for finished_sandwiches in finished_sandwiches:
    print(f"{finished_sandwiches.title()} is ready")