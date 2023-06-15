prompt = "\nHello! What is your name?"
prompt += "\nEnter 'quit' to end the program: "


def greet_user():
    greet_active = True
    """ Ask a users name """
    while greet_active:
        message = input(prompt)
    
        if message == 'quit':
            greet_active = False
        else:
            print(f"Nice to meet you {message}!")

greet_user()

def greet_user1(username):
    print(f"\nHello, {username.title()}")

greet_user1('jesse')

def favorite_book(title):
    print(f"\nOne of my favorite books is {title}.")

favorite_book('Grapes of Wrath')