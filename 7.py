import pandas as pd
import matplotlib.pyplot as plt
# 计算和分析每个城市2022年和2023年的租金情况，并采用合适的图或表形式进行展示。
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.figure(dpi=1000)
#读取数据
df_bj = pd.read_csv('lianjia/bj.csv')
df_bj_2022 = pd.read_json('RawData/BeijingHouseInfo.json', lines=True)
df_sh = pd.read_csv('lianjia/sh.csv')
df_sh_2022 = pd.read_json('RawData/ShanghaiHouseInfo.json', lines=True)
df_gz = pd.read_csv('lianjia/gz.csv')
df_gz_2022 = pd.read_json('RawData/GuangzhouHouseInfo.json', lines=True)
df_sz = pd.read_csv('lianjia/sz.csv')
df_sz_2022 = pd.read_json('RawData/ShenzhenHouseInfo.json', lines=True)

df_bj_mean = df_bj['price_per_m2'].mean()
df_sh_mean = df_sh['price_per_m2'].mean()
df_gz_mean = df_gz['price_per_m2'].mean()
df_sz_mean = df_sz['price_per_m2'].mean()
df_bj_2022_mean = df_bj_2022['price_per_m2'].mean()
df_sh_2022_mean = df_sh_2022['price_per_m2'].mean()
df_gz_2022_mean = df_gz_2022['price_per_m2'].mean()
df_sz_2022_mean = df_sz_2022['price_per_m2'].mean()
df = pd.DataFrame({'2022': [df_bj_2022_mean, df_sh_2022_mean, df_gz_2022_mean, df_sz_2022_mean], '2023': [df_bj_mean, df_sh_mean, df_gz_mean, df_sz_mean]}, index=['北京', '上海', '广州', '深圳'])
df.plot(kind='bar', rot=0)
#输出柱状图，显示均价
plt.title('2022和2023四大城市房租均价 元/m2')
plt.ylabel('均价 元/m2')
plt.xlabel('城市')
plt.show()
