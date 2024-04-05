from csv_to_class import csv_to_classes

# 读取CSV文件
residents = []
roads = []
facilities = []
residents, facilities, roads = csv_to_classes('city_map.csv')
print("location:",roads[5].depending_facilities)
