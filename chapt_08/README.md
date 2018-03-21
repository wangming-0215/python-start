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

4.  形参： 函数完成工作所需要的一些信息
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
        person = {'first': first_name, 'last': last_name)}
        if age:
            person['age'] = age
        return person
    ```

4.  结合使用函数和 while 循环

    ```py
    def get_formatted_name(f_name, l_name):
        full_name = f_name + ' ' + l_name
        return full_name

    while True:
        print('please tell me your name: ')
        print('\n(Enter \'q\' at any time to quit)')

        f_name = input('First name: ')
        if f_name = 'q':
            break

        l_name = input('Last name: ')
        if l_name = 'q':
            break

        formatted_name = get_formatted_name(f_name, l_name)
        print('\nHello, ' + formatted_name + '!')
    ```

## 传递列表

1.  将列表传递个函数后，函数就能直接使用访问列表的内容

    ```py
    def greet_users(names):
        for name in names:
            msg = 'Hello, ' + name.title()
            print(msg)

    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)
    ```

2.  在函数中修改列表：在函数中对这个列表的所做的任何修改都是永久性的。

    ```py
    # 不使用函数
    # 首先创建一个列表，其中包含要打印的设计
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    # 模拟打印每个设计，直到没有未打印的设计为止
    # 打印每个设计后，都将其一定到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根基设计制作3D打印模型的过程
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

    # 显示打印好的所有模型
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

    # 使用函数
    def print_models(unprinted_designs, completed_models):
        while unprinted_designs:
            current_design = unprinted_designs.pop()
            print('Printing model: ' + current_design)
            completed_models.append(current_design)

    def show_completed_models(completed_models):
        print('\nThe following models have been printed: ')
        for completed_model in completed_models:
            print(completed_model)

    unprint_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprint_designs, completed_models)
    show_completed_models(completed_models)
    ```

3.  每个函数都应值负责一项具体的工作
4.  禁止函数修改列表： 向函数传递列表的副本而不是原件，这样函数所做的修改都只影响副本，而丝毫不影响原件.（_虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此_）
    ```py
    function_name(list_name[:])
    ```
