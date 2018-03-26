# 测试代码

## 测试函数

```py
# name_function.py

# 待测试的函数
def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()
```

1.  单元测试和测试用例：
    * 单元测试：用于核实函数的某个方面没有问题
    * 测试用例：是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求
2.  要为函数编写测试用例：
    * 可先导入模块`unittest`以及要测试的函数，
    * 再创建一个继承`unittest.TestCase`的类，
    * 并编写一系列方法对函数行为的不同方面进行测试。

```py
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    ''' 测试name_function.py'''
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

3.  测试未通过意味着编写的新代码有错。因此，测试未通过时，不要修改测试，而是应该修复导致测试不能通过的代码：
    * 检查对函数的修改，找出导致函数行为不符合预期的修改

## 测试类

```py
# survey.py
class AnonymousSurvy():
    ''' 收集匿名调查问卷的答案 '''
    def __init__(self, question):
        ''' 存储一个问题，并未存储答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        ''' 显示调查问卷'''
        print(self.question)

    def store_response(self, new_response):
        responses.append(new_response)

    def show_results(self):
        print('Survey results: ')
        for response in responses:
            print('- ' + response)

# language_survey.py
from survey import AnonymousSurvey
question = 'What language did you fisrt learn to speak?'
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter \'q\' at any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response()

print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()
```

1.  各种断言方法：

|          方法           |          用途          |
| :---------------------: | :--------------------: |
|    assertEqual(a, b)    |      核实 a == b       |
|  assertNotEqual(a, b)   |       核实 a!=b        |
|      assertTrue(x)      |     核实 x 为 True     |
|     assertFalse(x)      |    核实 x 为 False     |
|  assertIn(item, list)   |  核实 item 在 list 中  |
| assertNotIn(item, list) | 核实 item 不在 list 中 |

2.  方法`setUp()`：只需创建对象一次，就可以在每个测试方法中使用。
    * 可在`setUp()`方法中创建一系列实例并设置它们的属性，在测试方法中直接使用这些实例。

**Note**：运行测试用例时，每完成一个单元测试，python 都打印一个字符串：

* 测试通过时打印一个句点；
* 测试引发一个错误时打印一个 E；
* 测试导致断言失败时打印一个 F。

```py
# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''测试AnonySurvey类'''

    def setUp(self):
        '''创建一个调查对象和一组问题，供测试方法使用'''
        question = 'What language did you first learn to speak'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Englist', 'Chinese', 'Spanish']

    def test_store_single_response(self):
        '''测试存储单个答案'''
        # question = 'What language did you first learn to speak'
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.response[0])
        self.assertIn(self.response[0], self.my_survey.responses)

    def test_store_three_responses(self):
        # question = 'What language did you first learn to speak'
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Chinese', 'Spanish']
        # for response in responses:
        #     my_survey.store_response(response)
        # for response in responses:
        #     self.assertIn(response, my_sruvey.responses)
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```
