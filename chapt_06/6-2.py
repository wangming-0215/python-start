yellow = {
    'type': 'dog',
    'host': 'wangming'
}

black = {
    'type': 'cat',
    'host': 'xiaoming'
}

pets = [yellow, black]

for pet in pets:
    print(pet['host'], 'has a', pet['type'], 'as a pet!')
