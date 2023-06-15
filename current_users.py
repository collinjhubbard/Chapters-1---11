current_users = ['lester', 'luke', 'justin', 'alex', 'collin']
new_users = ['lester', 'andrea', 'joe', 'justin', 'tony']
for user in new_users:
    if user in current_users:
        print(f"Sorry, that username is taken. Please choose another")
    else:
        print(f"That username is available")

users = ['lester', 'luke', 'justin', 'alex', 'collin', 'admin']
if users == []:
        print(f"We need to find some users!")
for user in users:
    if user == 'admin':
        print(f"Hello, {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello, {user.title()}! Thanks for logging in again!")

ordinal_numbers = []
for value in range(1,11):
    if value == 1:
        print(f"{value}st\n")
    elif value == 2:
        print(f"{value}nd\n")
    elif value == 3:
        print(f"{value}rd\n")
    else:
        print(f"{value}th\n")
    ordinal_numbers.append(value)