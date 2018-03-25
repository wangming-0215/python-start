file_name = 'files/guest_book.txt'

while True:
    guest_name = input('Please Enter your name: ')
    if guest_name:
        with open(file_name, 'a', encoding='utf-8') as file_object:
            print('Welcome!' + guest_name)
            file_object.write(guest_name + '\n')
