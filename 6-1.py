import pandas as pd
import matplotlib.pyplot as plt
# 计算和分析每个城市不同朝向的单位面积均价情况，并采用合适的图或表形式进行展示。
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.figure(dpi=1000)
#读取数据
df = pd.read_csv('lianjia/sz.csv')
#按direction分组，按占比绘制饼图
df_south = df['price_per_m2'].where(df['direction'].str.contains('南')).count()
df_north = df['price_per_m2'].where(df['direction'].str.contains('北')).count()
df_east = df['price_per_m2'].where(df['direction'].str.contains('东')).count()
df_west = df['price_per_m2'].where(df['direction'].str.contains('西')).count()
#构造数据
df_direction = [df_south, df_north, df_east, df_west]
df_direction = pd.DataFrame(df_direction, index=['南', '北', '东', '西'], columns=['price_per_m2'])
df_direction.plot.pie(y='price_per_m2', autopct='%.2f%%')
plt.title('深圳各朝向租房占比')
plt.show()
