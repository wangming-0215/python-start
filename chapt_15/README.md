# 数据可视化

1.  `plot(list)`：尝试根据 list 中数据绘制出有意义的图形
2.  `matplotlib.pyplot.show()`：打开`matplotlib`查看器，并显示图形
3.  向`plot()`提供一系列数字时，它假设第一个数据点对应的 x 坐标值为 0。要改变这种默认行为，可以给`plot(input, output)`同事提供输入值和输出值
4.  使用`scatter()`绘制散点图：
    * 参数`c`: 点的颜色,`c=(r, g, b)`：颜色分量，越接近 0，指定的颜色越深
    * `cmap`：颜色映射，一系列颜色，从起始颜色渐变到结束颜色。要使用颜色映射，需要告诉 pyplot 应该如何设置数据集中每个点的颜色。`plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)`
    * 参数`edgecolor`：点轮廓的颜色
    * 实参`s`：设置绘制图形时使用的点的尺寸
    * 要绘制一系列的点，可向`scatter()`传递两个分别包含 x 值和 y 值的列表
    * `plt.savefig(figure_path, bbox_inches='tight')`：第一个参数图标名称，第二个参数将图标多余的空白区域裁剪掉
    ```py
    x_value = [1, 2, 3, 4, 5]
    y_value = [1, 4, 9, 16, 25]
    plt.scatter(x_value, y_value, s=100)
    ```
5.  自动计算数据：
    ```py
    x_values = list(range(1, 5001))
    y_values = [x ** 3 for x in x_values]
    ```
6.  随机漫步：每次行走都完全是随机的，没有明确的方向，结果是由一系列决策决定的。
7.  `pygal`：[pygal](http://www.pygal.org)
