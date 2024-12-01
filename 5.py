import pandas as pd
import matplotlib.pyplot as plt
# 计算和分析每个城市不同板块(district)的均价情况，并采用合适的图或表形式进行展示。
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.figure(dpi=1000)
#读取数据
df = pd.read_csv('lianjia/dg.csv')
#按district分组，计算均价
df_mean = df.groupby('district')['total_price'].mean()
#按均价降序排列
df_mean = df_mean.sort_values(ascending=False)
#绘制横向条形图
df_mean.plot.barh()
for x, y in enumerate(df_mean):
    plt.text(y + 64, x - 0.3, '%.2f' % y, ha='center', va='bottom', fontsize=2)
plt.title('东莞各区域房租均价 元/月')
plt.yticks(fontsize=2)
plt.xlabel('均价 元/月')
plt.ylabel('板块')
plt.show()



