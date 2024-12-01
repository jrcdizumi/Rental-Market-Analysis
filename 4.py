import pandas as pd
import matplotlib.pyplot as plt
#比较5个城市一居、二居、三居的情况，包含均价、最高价、最低价、中位数等信息，包含租金的均价、最高价、最低价、中位数等信息，单位面积租金（元/平米）的均价、最高价、最低价、中位数等信息。采用合适的图或表形式进行展示。
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.figure(dpi=1000)
#读取数据
df_bj = pd.read_csv('lianjia/bj.csv')
df_sh = pd.read_csv('lianjia/sh.csv')
df_gz = pd.read_csv('lianjia/gz.csv')
df_sz = pd.read_csv('lianjia/sz.csv')
df_dg = pd.read_csv('lianjia/dg.csv')
#筛选出一居室 layout中包含1室或1房的数据
df_bj = df_bj.where(df_bj['layout'].str.contains('3室|3房'))
df_sh = df_sh.where(df_sh['layout'].str.contains('3室|3房'))
df_gz = df_gz.where(df_gz['layout'].str.contains('3室|3房'))
df_sz = df_sz.where(df_sz['layout'].str.contains('3室|3房'))
df_dg = df_dg.where(df_dg['layout'].str.contains('3室|3房'))
#筛选名字中不包含合租的数据
df_bj = df_bj.where(df_bj['name'].str.contains('合租') == False)
df_sh = df_sh.where(df_sh['name'].str.contains('合租') == False)
df_gz = df_gz.where(df_gz['name'].str.contains('合租') == False)
df_sz = df_sz.where(df_sz['name'].str.contains('合租') == False)
df_dg = df_dg.where(df_dg['name'].str.contains('合租') == False)
#计算均价
df_bj_mean = df_bj['total_price'].mean()
df_sh_mean = df_sh['total_price'].mean()
df_gz_mean = df_gz['total_price'].mean()
df_sz_mean = df_sz['total_price'].mean()
df_dg_mean = df_dg['total_price'].mean()
#计算最高价
df_bj_max = df_bj['total_price'].max()
df_sh_max = df_sh['total_price'].max()
df_gz_max = df_gz['total_price'].max()
df_sz_max = df_sz['total_price'].max()
df_dg_max = df_dg['total_price'].max()
#计算最低价
df_bj_min = df_bj['total_price'].min()
df_sh_min = df_sh['total_price'].min()
df_gz_min = df_gz['total_price'].min()
df_sz_min = df_sz['total_price'].min()
df_dg_min = df_dg['total_price'].min()
#计算中位数
df_bj_median = df_bj['total_price'].median()
df_sh_median = df_sh['total_price'].median()
df_gz_median = df_gz['total_price'].median()
df_sz_median = df_sz['total_price'].median()
df_dg_median = df_dg['total_price'].median()

#构造数据
data_mean = [df_bj_mean, df_sh_mean, df_gz_mean, df_sz_mean, df_dg_mean]
data_max = [df_bj_max, df_sh_max, df_gz_max, df_sz_max, df_dg_max]
data_min = [df_bj_min, df_sh_min, df_gz_min, df_sz_min, df_dg_min]
data_median = [df_bj_median, df_sh_median, df_gz_median, df_sz_median, df_dg_median]
#构造索引
index = ['北京', '上海', '广州', '深圳', '东莞']
#构造DataFrame
df = pd.DataFrame({'均价': data_mean}, index=index)
#绘制柱状图，柱顶显示数值
df.plot.bar(rot=0)
for y in data_mean:
    plt.text(data_mean.index(y), y + 0.1, '%.2f' % y, ha='center', va='bottom')
plt.title('5个城市三居的房租均价情况 元/月')
plt.show()
df = pd.DataFrame({'最高价': data_max}, index=index)
df.plot.bar(rot=0)
for y in data_max:
    plt.text(data_max.index(y), y + 0.1, '%.2f' % y, ha='center', va='bottom')
plt.title('5个城市三居的房租最高价情况 元/月')
plt.show()
df = pd.DataFrame({'最低价': data_min}, index=index)
df.plot.bar(rot=0)
for y in data_min:
    plt.text(data_min.index(y), y + 0.1, '%.2f' % y, ha='center', va='bottom')
plt.title('5个城市三居的房租最低价情况 元/月')
plt.show()
df = pd.DataFrame({'中位数': data_median}, index=index)
df.plot.bar(rot=0)
for y in data_median:
    plt.text(data_median.index(y), y + 0.1, '%.2f' % y, ha='center', va='bottom')
plt.title('5个城市三居的房租中位数情况 元/月')
plt.show()




