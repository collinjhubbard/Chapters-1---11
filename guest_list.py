guest_list = ['Fred Rogers', 'James Baldwin', 'Chris Thiel', 'Regina Spektor', 'Oscar Wilde', 'Rosa Luxembourg']
guest_list.insert(0, 'Justin Ravitz')
guest_list.insert(2, 'Jane Austen')
guest_list.append('Ken Cockrel')
guest_list.remove('Rosa Luxembourg')
for guest in guest_list:
    print(f"Thank you so much for coming to dinner, {guest.title()}. You have no idea how much this means to me!")
    print(f"That is, {guest.title()}, if you would indeed agree to come?\n")
for guest in guest_list:
        print(f"I'm so sorry {guest} that I was unable to put this together")

print(f"Thank you, everyone. Even though it didn't work out it still means a lot.")