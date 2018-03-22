class Restaurant():
    def __init__(self, restaurant_name, cuisint_type):
        self.restaurant_name = restaurant_name
        self.cuisint_type = cuisint_type

    def descirbe_restaurant(self):
        msg = self.restaurant_name.title() + ' serves wonderful ' + self.cuisint_type
        print(msg)

    def open_restaurant(self):
        msg = self.restaurant_name.title() + ' is open.'
        print(msg)


restaurant = Restaurant('wangming123', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisint_type)

restaurant.descirbe_restaurant()
restaurant.open_restaurant()
