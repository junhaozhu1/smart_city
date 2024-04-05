from csv_to_class import csv_to_classes
from mapTransform import map_transform

# 读取CSV文件
residents = []
roads = []
facilities = []
residents, facilities, roads = csv_to_classes('city_map.csv')
print("location:",facilities)

map = map_transform(residents, facilities, roads)
# for resident in residents:
#     # calc nearest hospital by walk
#     astar(resident, facilities, roads)
