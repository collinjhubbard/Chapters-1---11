favorite_places = {
    'collin': ['detroit', 'greece','cancun'],
    'kelly': ['new york','france','cancun'],
    'carly': ['paris','turkey','big bear'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

#OR

favorite_places = {
    'collin': {
        'city':'detroit',
        'country':'greece',
        'vacation':'cancun',
    },
    'kelly': {
        'city':'new york',
        'country':'france',
        'vacation':'cancun',
    },
    'carly': {
        'city':'paris',
        'country':'turkey',
        'vacation':'big bear',
    },
}

for key, value in favorite_places.items():
    print(f"\n{key.title()}'s favorite places are:")
    city = f"{value['city']}"
    country = f"{value['country']}"
    vacation = f"{value['vacation']}"

    print(f"\tCity: {city.title()}")
    print(f"\tCountry: {country.title()}")
    print(f"\tVacation: {vacation.title()}")