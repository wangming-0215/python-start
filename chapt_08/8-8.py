def make_album(singer, album_name):
    album = {
        'singer': singer,
        'album_name': album_name
    }
    return album


while True:
    print('Please tell me some informations: ')
    print('(Enter \'q\' at any time to quit)\n')

    singer = input('Singer name: ')
    if singer == 'q':
        break

    album_name = input('Album name: ')
    if album_name == 'q':
        break

    album = make_album(singer, album_name)
    print(album)
    print('----------------------------')
