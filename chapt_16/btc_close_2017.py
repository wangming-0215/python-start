import json
import math
from itertools import groupby
import pygal

# 将数据加载到一个列表中
filename = 'btc_close_2017_requests.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# 绘制折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
N = 20  # x 轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图.svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（¥）：'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::20]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')


def draw_line(x_date, y_date, title, y_legend):
    xy_map = []
    for key, group in groupby(sorted(zip(x_date, y_date)), key=lambda _: _[0]):
        y_list = [v for _, v in group]
        xy_map.append([key, sum(y_list) / len(y_list)])

    x_unique, y_mean = [*zip(*xy_map)]
    chart = pygal.Line()
    chart.title = title
    chart.x_labels = x_unique
    chart.add(y_legend, y_mean)
    chart.render_to_file(title + '.svg')
    return chart


idx_month = dates.index('2017-12-01')
draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值', '月日均值')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], '收盘价周日均值', '周日均值')

wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], '收盘价星期均值', '星期均值')

line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值.svg')

with open('Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in ['收盘价折线图.svg', '收盘价对数变换折线图.svg', '收盘价月日均值.svg', '收盘价周日均值.svg', '收盘价星期均值.svg']:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')
