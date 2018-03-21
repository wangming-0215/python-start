# 函数

## 定义函数

1.  关键字`def`告诉 python，要定义一个函数（函数名和需要的参数）

    ```py
    def greet_user():
        print('Hello')

    greet_user() # Hello
    ```

2.  函数调用让 python 执行函数的代码。要调用函数，可依次指定函数名以及用括号括起来的必要信息
3.  向函数传递信息：

    ```py
    def greet_user(username):
        print('Hello ' + username.title() + '!')

    greet_user('wangming') # Hello Wangming!
    ```

4.  形参： 函数完成工作所需要的一项信息
5.  实参： 调用函数时传递给函数的信息
6.  传递实参：

    * 位置实参：要求实参的顺序与形参的顺序相同（位置实参的顺序很重要）
    * 关键字实参： 每个实参由变量名和值组成；还可以使用列表和字典（直接在实参中将名称和值关联起来）

      ```py
      def describe_pet(animal_type, pet_name):
          print('\nI have a ' + animal_type + '.')
          print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

      describe_pet(pet_name='harry', animal_type='hamster')
      ```

7.  默认值：在调用函数中给形参提供了实参是，python 将使用指定的实参值，否则使用默认值（使用默认值时，在形参列表中必须先列出没有默认值的形参，在列出有默认值的形参。这让 python 依然能够正确的解读位置参数）

    ```py
    def describe_pet(pet_name, animal_type = 'dog'):
        print('\nI have a ' + animal_type + '.')
        print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

     describe_pet(pet_name='harry')
     describe_pet('willie')
    ```

## 返回值

1.  函数可以处理一些数据，并返回一个或者一组值

    ```py
    def get_formatted_name(first_name, last_name):
        full_name = first_name + ' ' + last_name
        return full_name.title()

    musician = get_formatted_name('jimi', 'hendrix')
    print(musician) # Jimi Hendrix
    ```

2.  让实参变成可选的

    ```py
    def get_formatted_name(first_name, last_name, middle_name = ''):
        if middle_name:
            full_name = first_name + ' ' + middle_name + ' ' + last_name
        else:
            full_name = first_name + ' ' + last_name
        return full_name

    musician = get_formatted_name('jimi', 'hendrix')
    print(musician) # Jimi Hendrix

    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician) # John Lee Hooker
    ```

3.  返回字典： 函数可以返回任何类型的值，包括字典和列表等较复杂的数据结构
    ```py
    def build_person(first_name, last_name, age=''):
        person = {'first': first_name, 'last': last_name, 'age': age)}
    ```
