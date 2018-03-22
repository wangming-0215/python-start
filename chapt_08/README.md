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
4.  禁止函数修改列表： 向函数传递列表的副本而不是原件，这样函数所做的修改都只影响副本，而丝毫不影响原件.（**虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此**）
    ```py
    function_name(list_name[:])
    ```

## 传递任意数量的参数

1.  python 允许函数调用语句中收集任意数量的实参（`*toppings`星号让 python 创建一个名为`toppings`的空元组，并将接收到的所有值都封装到这个元组中）

    ```py
    def make_pizza(*toppings)
        print(toppings)

    make_pizza('mushrooms', 'green peppers', 'extra cheese') # ('mushrooms', 'green peppers', 'extra cheese')
    ```

2.  结合使用位置实参和任意数量实参：在函数定义中，必须将接纳任意数量实参的形参放在最后，python 先匹配位置实参和关键字实参，在将余下的实参都收集到最后一个参数中（javascript rest ???)

    ```py
    def make_pizza(size, *toppings):
        print('\nMaking a ' + str(size) + '-inch pizza with the following toppings: ')
        for topping in toppings:
            print('- ' + topping)
    ```

3.  使用任意数量关键字实参：有时候需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息，在这种情况下，可将函数编写成能够接受任意数量的键值对---调用语句提供多少就接受多少（形参`**user_info`中的两个型号让 python 创建一个名为`user_info`的空字典，并将接收到的所有名称-值（关键字传参）都封装到这个字典中）

    ````py
    def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = lase
    for key, value in user_info.items:
    profile[key]=value

            return profile

        user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
        ```
    ````

## 将函数存储在模块中

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在高层逻辑上，复用性强。

1.  导入整个模块：

    * 模块：要让函数是可导入的，要先创建模块。模块就是扩展名为`.py`的文件，包含要导入到程序中的代码

      ```py
      # pizza.py
      def make_pizza(size, *toppings);
          print('\nMaking a ' + size + '-inch pizza with the following toppins: ')
          for topping in toppings:
              print('- ' + topping)

      # making_pizza.py
      import pizza # 导入模块
      pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
      ```

    * 导入模块的方法：
      * 导入整个模块：编写一条`import`语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。`import module_name`
      * 导入特定函数： `from module_name import function_0, function_1, function_2`
      * 使用`as`给函数指定别名： 如果要导入的函数名称可能与程序中的现有的名称冲突，或者函数名太长，可指定简短且独一无二的别名（函数的另一个名字）。 `from module_name import function_0 as func`
      * 使用`as`给模块指定别名： `import module_name as mod`
      * 导入模块中的所有函数：`from module_name import *`（由于导入了每个函数，所以可直接使用函数名调用函数，无需使用句点表示法。**如果模块中有函数名称与你的项目中使用的名称相同，可能会导致意想不到的结果：python 可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数**

## 函数编写指南

1.  给函数指定描述性名称，且只在其中使用小写字母和下划线
2.  每个函数都应包含简要阐述其功能的注释，该注释紧跟在函数定义后面，并采用文档字符串格式
3.  给形参指定默认值时，等号两边不要有空格
4.  如果形参很多，可在函数定义中输入左括号后按回车键，并在下一行按两次 Tab 键，从而将形参列表和只缩进一层的函数体区分开来。
5.  如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
6.  所有的`import`语句都应放在开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序
