import pandas as pd
import matplotlib.pyplot as plt

def drawMap(csv_path = 'map_data.csv'):
    # 从 CSV 文件中读取地图数据
    df = pd.read_csv(csv_path, index_col=False)

    # 提取医院、学校、街道和地铁线路的数据
    hospitals = df[df['Type'] == 'Hospital']
    schools = df[df['Type'] == 'School']
    streets = df[df['Type'] == 'Street']
    subways = df[df['Type'] == 'Subway']

    def write_label(start_x, start_y, end_x, end_y, row):
        if start_x == end_x and start_y != end_y:
            if row['Type'] == 'Street':
                ax.text(start_x, ((start_y + end_y) / 2)+0.5, row['Name'], rotation=90, fontsize=10)
            else:
                ax.text(start_x, (start_y + end_y) / 2, row['Name'], rotation=90, fontsize=10)
        elif start_y == end_y and start_x != start_y:
            if row['Type'] == 'Street':
                ax.text((start_x + end_x) / 2, start_y, row['Name'], fontsize=10)
            else:
                ax.text((start_x + end_x) / 2, start_y+0.5, row['Name'], fontsize=10)
        elif start_x != end_x and start_y != end_y:
            if row['Type'] == 'Street':
                ax.text((start_x + end_x) / 2, ((start_y + end_y) / 2)+1, 'Street', fontsize=10)
            else:
                ax.text((start_x + end_x) / 2, (start_y + end_y) / 2, row['Name'], fontsize=10)

    # 绘制地图
    fig, ax = plt.subplots(figsize=(10, 8))

    # 绘制街道
    for i, row in streets.iterrows():
        start_x, start_y = row['Start_X'], row['Start_Y']
        end_x, end_y = row['End_X'], row['End_Y']
        ax.plot([start_x, end_x], [start_y, end_y], color='black', linestyle='--', linewidth=1, label='Street')
        write_label(start_x, start_y, end_x, end_y, row)

    # 绘制地铁线路
    for i, row in subways.iterrows():
        start_x, start_y = row['Start_X'], row['Start_Y']
        end_x, end_y = row['End_X'], row['End_Y']
        ax.plot([start_x, end_x], [start_y, end_y], color='yellow', linestyle='-', linewidth=3, alpha=0.5, label='Subway')
        write_label(start_x, start_y, end_x, end_y, row)

    # draw buildings
    for i, row in hospitals.iterrows():
        if row['Type'] == 'Hospital':
            ax.scatter(row['Start_X'], row['Start_Y'], color='red', marker='H', s=200, label='Hospital')
            ax.text(row['Start_X'], row['Start_Y'], row['Name'], fontsize=12)

    for i, row in schools.iterrows():
        ax.scatter(row['Start_X'], row['Start_Y'], color='blue', marker='o', s=200, label='School')
        ax.text(row['Start_X'], row['Start_Y'], row['Name'], fontsize=12)

    # 设置标题和坐标轴标签
    ax.set_title('Simulated Map with Hospitals, Schools, Streets and Subways')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # 显示地图
    plt.grid(True)
    plt.show()

# 调用函数绘制地图
drawMap()