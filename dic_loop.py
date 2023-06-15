users = {
    'chubbard': {
        'first':'collin',
        'last':'hubbard',
        'location':'chicago',
    },
    'lleffler': {
        'first':'luke',
        'last':'leffler',
        'location':'grand rapids'
    },
    'aeberly': {
        'first':'alex',
        'last':'eberly',
        'location':'grand rapids'
    },
}

for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")