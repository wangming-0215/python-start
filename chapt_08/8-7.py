def make_album(singer, album_name, song_number=''):
    ablum = {
        'singer': singer,
        'album_name': album_name
    }

    if song_number:
        ablum['song_number'] = song_number

    return ablum


albumA = make_album('singerA', 'albumA', 10)
albumB = make_album('singerB', 'albumB')

print(albumA)
print('-----------------')
print(albumB)
