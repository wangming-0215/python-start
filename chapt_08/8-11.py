def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        magician = magician.title() + ' the Great'
        great_magicians.append(magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['harry', 'david', 'teller']
great_magicias = make_great(magicians[:])
# great_magicias = make_great(magicians)
print('The Great Magicians: ')
show_magicians(great_magicias)

print('\nThe Origin Magicians: ')
show_magicians(magicians)
