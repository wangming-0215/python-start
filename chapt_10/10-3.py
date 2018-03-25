file_name = 'files/guest.txt'
guest_name = input('Enter your name: ')

if guest_name:
    with open(file_name, 'a', encoding='utf-8') as file_object:
        file_object.write(guest_name + '\n')
else:
    print('You didn\'t enter anything!')
