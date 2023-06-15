bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bike was a {bicycles[0].title()}."
print(message)

names = ['alex', 'luke', 'lester', 'justin', 'joe']
friends_message = f"I most recently saw {names[0].title()}, {names[1].title()}, and {names[2].title()},  and before that I had just spoken to {names[-1].title()}."
print(friends_message)

ebikes = ['aventon', 'lectric', 'ride1', 'tern']
for ebike in ebikes:
    if ebike == 'ride1':
        print(ebike.upper())
    else:
        print(ebike.title())

lectric_message = f"{ebikes[1].title()} ebikes are some of the most affordable on the market."
aventon_message = f"{ebikes[0].title()} ebikes are very popular amongst Chicagoans and influencers."
print(lectric_message)
print(aventon_message)

ebikes.insert(0, 'radpower')
print(ebikes)
