integer = input('Please input an integer: ')

if integer:
    integer = int(integer)
    if integer % 10 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('nothing input')
