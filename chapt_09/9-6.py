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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisint_type, flavors=[]):
        super().__init__(restaurant_name, cuisint_type)
        self.flavors = flavors

    def show_flavors(self):
        print('\nIce cream with the following flavors: ')
        for flavor in self.flavors:
            print(' - ' + flavor)


flavors = ['plain', 'orange', 'strawberry']
ice_cream_stand = IceCreamStand('wang ming', 'ice cream', flavors)

ice_cream_stand.descirbe_restaurant()
ice_cream_stand.show_flavors()
