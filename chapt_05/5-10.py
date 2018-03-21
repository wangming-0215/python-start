current_users = ['David', 'John', 'Mary', 'Harry', 'Eric']
new_users = ['Jack', 'John', 'Harry', 'wangming', 'xiaoming']

for new_user in new_users:
    if new_user in current_users:
        print('Need other name!')
    else:
        print('Ok')
