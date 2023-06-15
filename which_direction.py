prompt = "\nWhich direction should we head towards?"
prompt += "\nNorth, South, East, or West? "
prompt += "\nEnter 'quit' to end the program: "


def which_direction():
    """ Ask a users name """
    message = input(prompt)
    
    if message == 'quit':
        print("Goodbye!") 
    elif message == 'North':
        print(f"Ah, {message}, towards the mountains!")
    elif message == 'South':
        print(f"Goodluck in the {message}. It is a terribly hot and swampy place.")
    elif message == 'East':
        print(f"The {message}! The land of steel, glass, and concrete.")
    elif message == 'West':
        print(f"Go {message}, Young Man!")
    else:
        print(f"You must give me a cardinal direction! (North, South, East, or West!)")

which_direction()