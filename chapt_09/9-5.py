class User():
    def __init__(self, name, age, email, location='HeFei'):
        self.name = name.title()
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print('\n' + self.name + ': ')
        print(' age: ' + str(self.age))
        print(' email: ' + self.email)
        print(' location: ' + self.location)

    def greet_user(self):
        print('Welcome back ' + self.name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


me = User('wang ming', 18, '775899982@qq.com')
print('me: ', me)
me.describe_user()
me.greet_user()

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print('\nlogin attempts: ' + str(me.login_attempts))

me.reset_login_attempts()
print('\nlogin attempts: ' + str(me.login_attempts))
