# 下载数据

1.  CSV 文件格式：将数据作为一系列逗号隔开的值。CSV 文件对人来说阅读起来比较麻烦，但是程序可以轻松获取其中的值。
2.  `csv.reader(file_object)`：创建一个与文件相关联的阅读器（reader）对象
3.  `next(reader)`：返回文件中的下一行，并将每项数据都作为一个元素存储在列表中
4.  `enumerate(list)`：获取列表中每个元素的索引和值
5.  时间序列特征初探：进行时间序列分析总是期望发现趋势，周期性和噪声，从而能够描述事实、预测未来、做出决策
6.  为了验证周期性假设，需要首先将非线性的趋势消除，对数变换是常用的处理方法之一
7.  `zip()`：
8.  `groupby()`：
