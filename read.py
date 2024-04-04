import pandas as pd

# 从 CSV 文件中读取数据
df = pd.read_csv('map_data.csv', index_col=False)

# 输出 DataFrame 的前几行数据
print(df.head())

# 提取医院数据
hospitals = df[df['Type'] == 'Hospital']
print("Hospitals:")
print(hospitals)

# 提取学校数据
schools = df[df['Type'] == 'School']
print("Schools:")
print(schools)

# 提取街道数据
streets = df[df['Type'] == 'Street']
print("Streets:")
print(streets)

# 提取地铁线路数据
subways = df[df['Type'] == 'Subway']
print("Subways:")
print(subways)
