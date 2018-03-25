# 文件和异常

## 从文件中读取数据

要使用文本文件中的信息，首先需要将信息读取到内存中。可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取

1.  读取整个文件：
    * `open(file_name)`：打开文件（然后才能访问它），在当前执行的文件所在的目录中查找指定的文件。返回一个表示文件的对象。
    * `with`：在不需要访问文件后将其关闭（涉及上下文管理器，这本书为深入解释，待以后探究）
    * `read()`：读取文件全部内容。（到达文件末尾时，返回一个空字符串）
    ```py
    with open('path/to/file') as file_object:
        contents = file_object.read()
        print(contents)
    ```
2.  文件路径：要让 python 打开不与程序文件在同一个目录下的文件，需要提供*文件路径*

    * 相对路径：相对于当前运行的程序所在的目录
    * 绝对路径
    * 原始字符串：在开头的单引号前面加上`r`。

3.  逐行读取：对文件对象使用`for`循环

    ```py
    with open(file_name) as file_object:
        for line in file_object:
            print(line)
    ```

4.  创建一个包含文件各行内容的列表：

    * 使用关键字`with`时，`open()`返回的文件对象只在`with`代码块中可用。如果要在`with`代码块外访问文件的内容，可在`with`代码块内将文件的各行内容存储在一个列表中。
    * `readlines()`：从文件中都每一行，并将其存储在一个列表中

    ```py
    with open(file_name) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line)
    ```

5.  使用文件内容：将文件读取到内存中，就可以以任何方式使用这些数据了。（读取文件时，python 将其中的所有文本都解读为字符串，所以特别注意读取数字的时候的类型转换）
6.  包含一百万位的大型文件：对于可以处理的数据量，python 没有任何限制，只要系统内存足够大，想处理多少数据都可以。

## 写入文件

1.  写入空文件：
    * `open(file_name, mode)`：第二个参数告诉 python 打开文件的模式
      * 读取模式： `'r'` （默认）
      * 写入模式： `'w'` （如果文件已经存在，python 将在返回文件对象之前清空文件）
      * 附加模式： `'a'`
      * 读写模式： `'r+'`(读取和写入)
    * 如果要写入的文件不存在，`open()`函数会自动创建。
    * `write()`：将字符串写入文件。不会再文本末尾添加换行符（python 只能将字符串写入文本文件）
2.  写入多行：要让每个字符串都单独占一行，需要在`write()`语句中包含换行符（`\n`, `\t` ...)
3.  附件到文件：给文件添加内容，而不是覆盖原有的内容，需要使用*附加模式*打开文件。附加模式打开文件时，不会清空文件的内容，而是在文件末尾追加内容

## 异常

异常：管理程序执行期间发生的错误，使用`try-except`代码块处理。

1.  使用 try-except 代码块：
    * 如果`try`代码块中的代码运行起来没有问题，python 将跳过`except`代码块；
    * 如果`try`代码块中的代码导致了错误，python 将查找这样的`except`代码块，并运行其中代码；
    * 如果`try-except`代码块后面还有其他代码，程序将继续执行。
    ```py
    try:
        print(5/0)
    except ZeroDivisionError:
        print('You can\'t divide by zero')
    ```
2.  使用异常避免崩溃：
3.  `else`代码块：依赖于`try`代码块成功执行的代码都应放在`else`代码块中。
4.  `try-except-else`大致的工作原理：
    * python 在尝试执行`try`代码块中的代码；只有可能引发异常的代码才需要放在`try`语句中。
    * 有时候，有一些仅在`try`代码块成功执行时才需要运行的代码，这些代码应放在`else`代码块中。
    * `except`代码块告诉 python，如果尝试运行`try`代码块中的代码时引发了指定的异常，该怎么办
5.  分析文本：
    * `split()`：以空格为分隔符将字符串拆分成多个部分，并将这些部分都存储在一个列表中。
6.  使用多个文件：
7.  `pass`语句：代码块中使用`pass`来让 python 什么都不做
8.  决定报告哪些错误：

## 存储数据

使用 json 来存储数据

1.  使用`json.dump()`和`json.load()`：
    * `json.dump(data, file_object)`：保存 json 数据
      * `data`：要存储的数据
      * `file_object`：用于存储数据的文件对象
    ```py
    import json
    numbers = [1,2,3,4,5,6]
    filename = 'number.json'
    with open(filename, 'w') as file_object:
        json.dump(numbers, file_object)
    ```
    * `json.load(file_object)`：读取 json 数据
