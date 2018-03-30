import csv
from datetime import datetime
import matplotlib.pyplot as plt

# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    # 获取CSV文件头
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # 提取并读取数据
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 绘制气温图表
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # 设置图形的格式
    title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()  # 绘制倾斜的日期标签，避免重叠
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.show()
