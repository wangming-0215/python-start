from random import randint
import pygal


class Die():
    '''骰子类'''

    def __init__(self, num_sides=6):
        '''骰子默认6个面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回一个位于1和骰子面数之间的随机数'''
        return randint(1, self.num_sides)


# 创建一个骰子
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
# 计算每个点数出现的次数
frequencies = []

for value in range(1, die.num_sides + 1):
    frequencey = results.count(value)
    frequencies.append(frequencey)

print(frequencies)

# 对分析的结果可视化
# 绘制直方图
hist = pygal.Bar()
# 直方图标题
hist.title = "Results of rolling one D6 1000 times"
# x 轴标签
hist.x_labels = [x for x in range(1, 7)]
# x 轴标题
hist.x_title = 'Result'
# y 轴标题
hist.y_title = 'Frequency of Result'
# 将一系列值添加到图表中
# 传递要给添加的值指定的标签和出现在图表中的值（列表）
hist.add('D6', frequencies)
# 渲染成文件
hist.render_to_file('die_visual.svg')
