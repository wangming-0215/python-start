# 类

## 创建类和使用类

1.  创建类

    * 在 python 中，首字母大写的名称指的是类，这个类定义中的括号是空的，表示从空白创建这个类（没有继承），类中的函数称为方法。
    * `__init__()`是一个特殊的方法，每次创建实例时，python 都会自动运行它
    * `self`:每个与类相关联的方法调用都会自动传递实参`self`，它是一个指向实例本身的引用（this？？？），让实例能够访问类中的属性和方法
    * python2.7 中定义类：`class Dog(object):`

    ```py
    # dog.py
    class Dog():
        '''一次模拟小狗的简单尝试'''

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def sit(self):
            print(self.name.title() + ' is now sitting.')

        def roll_over(self):
            print(self.name.title() + ' rolled over!')
    ```

2.  根据类创建实例：可将类视为有关如何创建实例的说明（实例的蓝图）

    ```py
    # dog.py
    dog = Dog('willie', 6)
    print('My dog\'s name is ' + dog.name.title() + '.') # My dog's name is Willie
    print('My dog is ' + str(dog.age) + ' years old.') # My dog is 6 years old

    dog.sit() # Willie is now sitting.
    dog.roll_over() # Willie rolled over!
    ```

## 使用类和实例

```py
# car.py
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer')

    def fill_gas_tank(self):
        print('fill gas tank')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

1.  给属性指定默认值： 类中的每个属性都必须有初始值，哪怕这个值是 0 或空字符串
    * 在`__init__`指定初始值，此时无需包含为它提供初始值的形参
2.  修改属性的值：

    * 直接修改属性的值：
      ```py
      my_new_car.odometer_reading = 23
      my_new_car.read_odometer() # This car has 23 miles on it
      ```
    * 通过方法修改属性的值：无需直接访问属性，而是将值传递给一个方法，由他在内部进行更新。可对方法进行扩展，使其在修改属性的值时做些额外的工作

    ```py
    my_new_car.update_odometer(23)
    my_new_car.read_odometer() # This car has 23 miles on it
    ```

## 继承

一个类继承另一个类时，将自动获得另一个类的所有属性和方法，原有的类称为*父类*，而新类称为*子类*。子类继承了其父类的所有属性和方法，同时也可以定义自己的属性和方法

1.  子类的方法`__init__()`：创建子类实例时，python 首先要完成的任务是给父类的所有属性赋值。创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称。

    ```py
    class ElectricCar(Car):
        def __init__(self， make, model, year):
            # super()帮助python将父类和子类关联起来
            super().__init__(make, model, year) # 初始化父类属性

    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name()) # 2016 Tesla Model S
    ```

2.  python2.7 中继承语法有所不同：函数`super()`需要两个参数：子类名和对象 self。（在 python2.7 中使用继承时，务必在定义父类时在括号内指定`object`： `class Car(object):`）

    ```py
    super(ElectricCar, self).__init__(make, model, year)
    ```

3.  给子类定义属性和方法：

    ```py
    class ElectricCar(Car):
        def __init__(self, make, model, year):
            '''
            初始化父类属性，并初始化子类特有的属性
            '''
            super().__init__(make, model, year)
            self.battery_size = 70

        def describe_battery(self):
            ''' 子类特有的方法'''
            print('This car has a ' + self.battery_size + '-kWh battery.')

    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name()) # 2016 Tesla Model S
    my_tesla.describe_battery() # This car has a 70-kWh battery
    ```

4.  重写父类方法：在子类中定义一个与父类方法同名的方法，即可重写父类的这个方法（python 不会考虑这个父类方法，而只关注在子类中定义的方法）。_使用继承时，可让子类保留从父类继承的精华，并提出不需要的糟粕_。

    ```py
    class ElectricCar(Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery_size = 70

        def describe_battery(self):
            print('This car has a ' + slef.battery_size + '-kWh battery.')

        def fill_gas_tank(self):
            ''' 重写父类的fill_gas_tank方法 '''
            print('This car dose not need a gas tank')
    ```

5.  将实例用作属性：在给类添加的细节越来越多时，属性和方法清单以及文件都越来越长，这时，可能需要将类的一部分作为一个独立的类提取出来。（可以将大型的类拆分成多个协同工作的小类）

    ```py
    class Battery():
        def __init__(self, battery_size=70):
            self.battery_size = battery_size

        def describe_battery(self):
            print('This car has a ' + self.battery_size + '-kWh battery.')

        def get_range(self):
            if self.battery_size == 70:
                range = 240
            elif self.battery_size == 85:
                range = 270

            message = 'This car can go approximately ' + str(range)
            message += ' miles on a full charge.'
            print(message)

    class ElectricCar(Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery = Battery()

    my_tesla = ElectricCar('tesla', 'model s', 2016)
    my_tesla.battery.describe_battery() # This car has a 70-kWh battery.
    my_tesla.battery.get_range() # This car can go approximately 240 miles on a full charge.
    ```

6.  从较高的逻辑层面（而不是语法层面）考虑；你考虑的不是 python，而是如何使用代码来表示实物。
7.  现实世界的建模方法并没有对错之分，有些方法效率更高，但要找出效率更高的表示法，需要经过一定的实践。只要代码像你希望的那样运行，就说明你做的很好。即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁；要编写出高效、准确的代码，都得经过这样的过程。
