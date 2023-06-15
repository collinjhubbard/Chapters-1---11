def make_sandwich(size, *ingredients):
    print(f"\nMaking {size} inch sub with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich(6, 'ham', 'salami', 'capocolo', 'spinach')

def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('collin', 'hubbard', height="5'5", eye_color='grey', hair_color='brown' )

print(user_profile)

def build_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

new_car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(new_car)
