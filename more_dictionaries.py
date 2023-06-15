glossary = {
    'list':'an array',
    'tuple':'an immutable array',
    'method':'an action performed on a piece of data',
    'variables':'a label for a value',
    'dictionaries':'an object',
    'for-loops':'a way to iterate through lists and dictionaries',
    'if-elif-else':'conditional test',
    'zen python':'style guide for python',
}

for key, value in glossary.items():
    print(f"\nKey:{key.title()}")
    print(f"Value:{value.title()}")

rivers = {'pearl river':'china', 'mekong river':'vietnam', 'missouri river':'united states'}
for key in rivers.keys():
    print(f"\nThe {key.title()}")
for value in rivers.values():
    print(f"\nIn {value.title()}")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'lester':'javascript',
    'luke':'r',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

if 'collin' not in favorite_languages.keys():
    print("Collin, please take your quiz!")
