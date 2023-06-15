prompt = "\nPlease enter your preffered pizza toppings"
prompt += "\tEnter 'quit' to end the program: "


while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"We'll add {message} to your pizza!")

prompt1 = "\nYour ticket price varies depending on your age. How old are you?"
prompt1 += "\nEnter 'quit' to end the program: "

while True:
    message = input(prompt1)
    
    if message == 'quit':
        break
    else:
        message = int(message)

    if message < 3:
        price = 0
    elif message <= 12:
        price = 10
    else:
        price = 15
    print(f"Your admission cost is {price}")
