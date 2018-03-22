class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email

    def decribe_user(self):
        print('\n' + self.first_name + ' ' + self.last_name)
        print(' Age: ' + str(self.age))
        print(' Email: ' + self.email)

    def greet_user(self):
        print('Welcome back ' + self.first_name + ' ' + self.last_name)


me = User('wang', 'ming', 18, '775899982@qq.com')

print(me)
me.decribe_user()
me.greet_user()
