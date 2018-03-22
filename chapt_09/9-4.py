class Restaurant():
    def __init__(self, name, cuisint_type):
        self.name = name
        self.cuisint_type = cuisint_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + ' serves wonderful ' + self.cuisint_type
        print(msg)

    def open_restaurant(self):
        msg = self.name + ' is opening.'
        print(msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


small_restaurant = Restaurant('small', 'samll pizza')
print('\nNumber served: ' + str(small_restaurant.number_served))

small_restaurant.set_number_served(500)
print('\nNumber served: ' + str(small_restaurant.number_served))

small_restaurant.increment_number_served(500)
print('\nNumber served: ' + str(small_restaurant.number_served))
