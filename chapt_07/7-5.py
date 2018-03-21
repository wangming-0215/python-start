running = True

while running:
    try:
        age = int(input('How old are you? '))
        if age < 3:
            print('Free')
        elif age >= 3 and age <= 12:
            print('$10')
        else:
            print('$15')
    except Exception as reason:
        print(reason)
        running = False
