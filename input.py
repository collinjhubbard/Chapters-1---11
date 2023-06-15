prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

prompt2 = "\nWhat kind of rental car would you like? "
what_kind = input(prompt2)

print(f"\tA {what_kind} is a great choice!")

hostess_prompt = input("\nHow many people are in your party? ")
hostess_prompt = int(hostess_prompt)

if hostess_prompt > 8:
    print(f"\tYou'll have to wait for a table.")
else:
    print(f"\tYour table is ready")

prompt3 = "\nEnter a number, and I'll tell you if guessed correctly: "
prompt3 += "\n Enter 'quit' to exit."

message = ""
while message != 'quit':
    message = input(prompt3)

    if message != 'quit':
        print(message)