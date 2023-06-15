cities = {
    'mexico city': {
        'country':'mexico',
        'population':'21500000',
        'fact':'most populous in north america'
    },
    'mumbai': {
        'country':'india',
        'population':'19900000',
        'fact':'governed by a municipal corporation'
    },
    'cairo': {
        'country':'egypt',
        'population':'20000000',
        'fact':'the city of a thousand minarets',
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()} is a wonderful place!")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"

    print(f"\tIt is located in {country.title()} and has a population of {population}. It is also {fact}!")

cities2 = {
    'mexico city': ['mexico','21500000','most populous in north america'],
    'mumbai': ['india','19900000','governed by a municipal corporation'],
    'cairo': ['egypt','20000000','the city of a thousand minarets'],
}

for city, city_info in cities2.items():
    print(f"\n{city.title()} is a wonderful place!")
    for info in city_info:
        print(f"\t{info}")