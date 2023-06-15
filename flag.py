prompt = "\nGuess a number between 1 and 100. I'll tell you if you guessed correctly "
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == '11':
        print(f"You won!")
        active = False
    elif message == 'quit':
        active = False
    else:
        print(f"\nThat's incorrect. Guess again! ")