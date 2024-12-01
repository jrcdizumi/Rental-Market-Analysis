import pandas as pd
import matplotlib.pyplot as plt
# 计算和分析每个城市不同朝向的单位面积均价情况，并采用合适的图或表形式进行展示。
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.figure(dpi=1000)
#读取数据
df = pd.read_csv('lianjia/dg.csv')
#按direction分组，计算均价
df_mean_south = df['price_per_m2'].where(df['direction'].str.contains('南')).mean()
df_mean_north = df['price_per_m2'].where(df['direction'].str.contains('北')).mean()
df_mean_east = df['price_per_m2'].where(df['direction'].str.contains('东')).mean()
df_mean_west = df['price_per_m2'].where(df['direction'].str.contains('西')).mean()
#构造数据
df_mean = [df_mean_south, df_mean_north, df_mean_east, df_mean_west]
df_mean = pd.DataFrame(df_mean, index=['南', '北', '东', '西'], columns=['price_per_m2'])
df_mean.plot.bar(rot=0)
#输出柱状图，显示均价
for x, y in enumerate(df_mean['price_per_m2']):
    plt.text(x, y + 0.1, '%.2f' % y, ha='center', va='bottom')
plt.title('东莞各朝向房租均价 元/m2')
plt.xlabel('均价 元/m2')
plt.ylabel('朝向')
plt.show()
#输出密度图
plt.figure(dpi=1000)
#调整线条粗细
plt.rcParams['lines.linewidth'] = 0.5
df_south = df['price_per_m2'].where(df['direction'].str.contains('南'))
df_north = df['price_per_m2'].where(df['direction'].str.contains('北'))
df_east = df['price_per_m2'].where(df['direction'].str.contains('东'))
df_west = df['price_per_m2'].where(df['direction'].str.contains('西'))
df_south.plot.density()
df_north.plot.density()
df_east.plot.density()
df_west.plot.density()

plt.title('东莞各朝向房租密度图 元/m2')
plt.xlabel('均价 元/m2')
plt.ylabel('密度')
plt.legend(['南', '北', '东', '西'])
plt.show()
