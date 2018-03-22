class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self, user):
        print('\n' + user + ' has the following privileges: ')
        for privilege in self.privileges:
            print(' - ' + privilege)


class User():
    def __init__(self, username, email, role='user'):
        self.username = username
        self.email = email
        self.role = role

    def descirbe_user(self):
        print('\n' + self.username)
        print(' - Email: ' + self.email)
        print(' - Role: ' + self.role)


class Admin(User):
    def __init__(self, username, email, role, privileges=[]):
        super().__init__(username, email, role)
        self.privileges = Privileges(privileges)


admin = Admin('wangming_0215', '775899982@qq.com', 'admin', [
              'can add post', 'can delete post', 'can ban user'])

admin.descirbe_user()
admin.privileges.show_privileges(admin.username)

user = Admin('xiaoming_0314', '1850889632@qq.com', 'user')
user.descirbe_user()
user.privileges.show_privileges(user.username)
