wangming = {
    'first_name': 'wang',
    'last_name': 'ming',
    'age': 18,
    'city': 'hefei'
}

xiaoming = {
    'first_name': 'xiao',
    'last_name': 'ming',
    'age': 16,
    'city': 'jinan'
}

daming = {
    'first_name': 'da',
    'last_name': 'ming',
    'age': 26,
    'city': 'shanghai'
}

persons = [wangming, xiaoming, daming]

for person in persons:
    print('first name:', person['first_name'], '\nlast name:',
          person['last_name'], '\nage:', person['age'], '\ncity:', person['city'])
    print('-----------------------')

print()

for person in persons:
    for key in person.keys():
        print(key, ':', person[key])
    print('-------------------')
