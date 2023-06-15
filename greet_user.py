prompt = "\nHello Traveller! What is your name?"
prompt += "\nEnter 'quit' to end the program: "


def greet_user():
    """ Ask a users name """
    message = input(prompt)
    
    if message == 'quit':
        print("Goodbye!") 
    else:
        print(f"Nice to meet you {message}!")

greet_user()