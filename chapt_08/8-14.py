def make_car(manufacturer, car_type, **other_info):
    car = {
        'maunfacturer': manufacturer,
        'type': car_type
    }

    for key, value in other_info.items():
        car[key] = value

    return car


car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
