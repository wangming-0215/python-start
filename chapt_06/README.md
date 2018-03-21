# 字典

在 python 中，字典是一系列键-值对。每个键都与一个值相关联，可以使用键来访问与之相关联的值。

字典是一种动态结构，可随时在视同添加键值对

1.  访问字典中的值

    ```py
    alien_0 = { 'color': 'green'}
    print(alien_0[color]) # green
    ```

2.  添加键值对

    ```py
    alien = {'color': 'green'}
    alien['points'] = 5
    print(alien) # {color: 'green', points: 5}
    ```

3.  修改字典中的值

    ```py
    alien = { 'color': 'green' }
    aline['color'] = 'yellow'
    ```

4.  删除键值对： `del`语句将相应的键值对彻底删除（必须制定字典名和要删除的键）

    ```py
    alien = { 'color': 'yellow', 'points': 5 }
    del alien['color']
    print(alien) # {points: 5}
    ```

5.  遍历字典：可遍历字典的所有键-值对、键或值（即使遍历字典时，键-值对的返回顺序也与存储顺序不同，python 不关心键-值对的存储顺序，而只跟踪键和值之间的关联关系）

    * `dic.items()`: 返回一个键-值对列表
    * `dic.keys()`: 遍历字典中所有的键（遍历字典时，会默认遍历所有的键，所以`for name in languages.keys()`和`for name in languages`的输出相同）
    * `dic.values()`: 遍历字典中所有的值，返回一个值列表（`set(list)`:将`list`转换成`set`集合）

6.  按顺序遍历字典中的所有键：
    * 在 for 循环中对返回的键进行排序。 `for name in sorted(languages.keys())`
