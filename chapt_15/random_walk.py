from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    '''生成随机漫步的类'''

    def __init__(self, num_point=5000):
        '''初始化随机漫步的属性'''
        self.num_point = num_point

        # 所有的随机漫步都始于（0， 0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有的点'''

        # 不断漫步，知道列表打到指定长度
        while len(self.x_values) < self.num_point:
            # 决定前进的方向和沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置窗口尺寸
    plt.figure(figsize=(10, 6))

    # 根据随机漫步中各点的先后顺序进行着色
    point_numbers = list(range(rw.num_point))
    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Blues, s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break
