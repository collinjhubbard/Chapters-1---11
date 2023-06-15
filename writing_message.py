prompt = "Hello, User, what is your name? "
prompt += "Enter 'quit' to exit: "

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    active = True
    while active:
        message = input(prompt)
        file_object.write(f"{message}\n")
        
        if message == 'quit':
            active = False
        else:
            print(f"So nice to meet you {message}")

responses_file = 'poll.txt'
prompt1 = "Why do you like programming? "
prompt1 += "Enter quit to exit: "
with open(responses_file, 'w') as file_object:
    polling_active = True

    while polling_active:
        message = input(prompt1)
        file_object.write(f"{message}\n")
        if message == 'quit':
            polling_active = False