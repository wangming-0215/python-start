done = False

while not done:
    fruit = input('Please input some fruit: ')
    if fruit == 'quit':
        done = True
    else:
        print('You will have',  fruit)
