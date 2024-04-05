from csv_to_class import csv_to_classes
from mapTransform import map_transform
from mapTransform import print_map

# 读取CSV文件
residents = []
roads = []
facilities = []
residents, facilities, roads = csv_to_classes('city_map.csv')


map = map_transform(residents, facilities, roads)
print_map(map)



# for resident in residents:
#     # calc nearest hospital by walk
#     astar(resident, facilities, roads)
