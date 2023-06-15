def city_country(city_name, country_name):
    full_name = f"{city_name}, {country_name}"
    return full_name.title()

location = city_country('philadelphia', 'u.s.a')
print(location)

def make_album(artist_name, album_title, number_songs=None):
    album = {'artist': artist_name, 'album':album_title}
    if number_songs:
        album['number_songs'] = number_songs
    return album
while True:
    print('\nEnter an artists name:')
    print("(enter 'q' at any time to quit) ")

    artists_name = input("Artists name: ")
    if artists_name == 'q':
        break
    album_name = input("Album title: ")
    if album_name == 'q':
        break
    full_album = make_album(artists_name, album_name)
    print(full_album)

