# 用户输入和 while 循环

## `input()`

函数`input()`让程序暂停运行，等待用户输入一些文本。获取用户输入后，python 将其存储在一个变量中。

1.  `input()`函数接受一个参数：要向用户显示的提示或者说明
2.  使用`input()`函数，python 会将用户输入解读为字符串
3.  `int()`函数将数字的字符串转换为数值表示
4.  求模运算符（%）：将两个数相除并返回余数

## `while`循环

1.  `for`循环用于针对集合中每个元素，而`while`循环不断地运行，知道指定条件不满足为止
2.  在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断程序是否处于活动状态。这个状态称为标志，充当程序的交通信号灯。这样在`while`语句中只需检查一个条件（标志的当前值是否为 True），并将所有的测试都放在其他地方，从而让程序变得简洁
3.  `break`退出循环：立即退出循环，不再运行循环中的余下的代码，也不管条件测试的结果如何。（`break`用于控制程序流程， 在任何 python 循环中都可以使用`break`语句）
4.  `continue`: 返回到循环开头，并根据条件测试结果决定是否继续执行循环（跳过当前循环，直接执行下一轮循环）
5.  要避免编写无限循环，务必对每个`while`循环进行测试，确保它按预期那样结束

## 使用`while`循环来处理列表和字典

1.  在列表之间移动元素

    ```py
    # 首先，创建一个待验证用户列表
    # 和一个用于存储已验证用户的空列表
    unconfirmed_users = ['alice', 'brain', 'candace']
    confirmed_users = []

    # 验证每个用户，直到没有未验证用户为止
    # 将每个经过验证的用户移到已验证用户列表中
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print('Verifying user:' + current_user.title())
        confirmed_users.append(current_user)

    # 显示所有已验证用户
    print('\nThe following users have been confirmed:')
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
    ```

2.  删除列表中所有的某个特定元素

    ```py
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')

    print(pets)
    ```

3.  使用用户输入来填充字典

    ```py
    responses = {}

    # 设置一个标志，指出调查是否继续
    polling_active = True

    while polling_active:
        # 提示输入被调查者的名字和回答
        name = input('\nWhat is your name? ')
        response = input('Which mountain would you like to climb someday? ')

        # 将答卷填入字典中
        responses[name] = response

        # 看看是否还有人要参与调查
        repeat = input('Would you like to let another person response?(yes/no) ')
        if repeat == 'no':
            polling_active = False

    # 调查结束，显示结果
    print('\n--- Poll Result ---')
    for name, mountain in responses.items():
        print(name + ' would like to climb ' + mountain + '.')
    ```
