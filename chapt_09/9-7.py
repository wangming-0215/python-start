class User():
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def decribe_user(self):
        print('\n' + self.first_name + ' ' + self.last_name)
        print(' username: ' + self.username)
        print(' Email: ' + self.email)

    def greet_user(self):
        print('Welcome back ' + self.first_name + ' ' + self.last_name)


class Admin(User):
    def __init__(self, first, last, username, email, privileges=[]):
        super().__init__(first, last, username, email)
        self.privileges = privileges

    def show_privileges(self):
        print(self.username + ' has the following privileges: ')
        for privilege in self.privileges:
            print(' - ' + privilege)


privileges = ['can add post', 'can delete post', 'can ban user']

admin = Admin('wang', 'ming', 'wangming_0215', '775899982@qq.com', privileges)
admin.decribe_user()

admin.show_privileges()
