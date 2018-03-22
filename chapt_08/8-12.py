def make_sandwich(*toppings):
    print('\nMaking a sandwich with the following toppings: ')
    for topping in toppings:
        print('- ' + topping)


make_sandwich('mushrooms')
make_sandwich('mushrooms', 'green peppers')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
