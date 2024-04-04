import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建一个包含地图数据的 pandas DataFrame
data = {
    'Location': ['Hospital A', 'Hospital B', 'School X', 'School Y'],
    'Type': ['Hospital', 'Hospital', 'School', 'School'],
    'X': [15, 25, 10, 30],
    'Y': [20, 30, 35, 25]
}
df = pd.DataFrame(data)

# 创建街道坐标
street1_x = np.arange(5, 15, 1)
street1_y = [20] * len(street1_x)

street2_x = np.arange(15, 25, 1)
street2_y = np.arange(20, 30, 1)

street3_x = np.arange(25, 35, 1)
street3_y = [30] * len(street3_x)

# 创建地铁坐标
subway_x = np.linspace(5, 15, 50)
subway_y = [20] * len(subway_x)

# 绘制地图
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制街道
ax.plot(street1_x, street1_y, color='gray', linestyle='--')
ax.plot(street2_x, street2_y, color='gray', linestyle='--')
ax.plot(street3_x, street3_y, color='gray', linestyle='--')

# 在街道旁边标注街道名称
ax.text(10, 20.5, 'Street 1', fontsize=10, rotation=0)
ax.text(20, 24, 'Street 2', fontsize=10, rotation=55)
ax.text(30, 31, 'Street 3', fontsize=10, rotation=0)

# 绘制地铁线路（黄色透明）
ax.plot(subway_x, subway_y, color='yellow', linestyle='-', linewidth=3, alpha=0.5, label='Subway')

# 在地铁旁边标注地铁
ax.text(10, 20, 'Subway', fontsize=10, rotation=0)

# 绘制医院和学校
for i, row in df.iterrows():
    if row['Type'] == 'Hospital':
        ax.scatter(row['X'], row['Y'], color='red', marker='H', s=200)
    else:
        ax.scatter(row['X'], row['Y'], color='blue', marker='o', s=200)
    ax.text(row['X'], row['Y'], row['Location'], fontsize=12)


# 设置标题和坐标轴标签
ax.set_title('Simulated Map with Hospitals and Schools')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# 显示地图
plt.grid(True)
plt.show()
