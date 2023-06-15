states = ['Alabama','Alaska','Arizona','Arkansas','California',
        'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
        'Hawaii','Idaho','Illinois','Indiana','Iowa', 'Kansas',
        'Kentucky','Louisiana','Maine','Maryland','Massachusetts',
        'Michigan','Minnesota','Mississippi','Missouri','Montana',
        'Nebraska','Nevada','New Hampshire','New Jersey']
for state in states:
    if state == 'Michigan':
        print(f"{state.title()}, the Great Lakes State")
    if state.lower() == 'alabama':
        print(f"{state.upper()}, ROLL TIDE!")
    else:
        print(f"{state.title()}")
