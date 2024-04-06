from csv_to_class import csv_to_classes
from mapTransform import map_transform
from mapTransform import print_map
from astar import a_star_search_euclidean
import math
from add_to_building import add_to_buildings, print_building_dit
T0 = ["Ho", "Po", "Fi"]
T1 = ["Sc", "Ma", "Cl"]
T2 = ["Pa", "In"]

# 读取CSV文件
residents = []
roads = []
facilities = []
residents, facilities, roads = csv_to_classes('city_map.csv')


map = map_transform(residents, facilities, roads)
print_map(map)

building_list = []
for i,  line in enumerate(map):
    for j, grid in enumerate(line):
        if grid and grid != '.':
            building_list.append((grid, (i,j)))

buildings_dict = {}
buildings_dict = add_to_buildings(building_list)
#print_building_dit(buildings_dict)

for houseId, facilities in buildings_dict.items():
    is_nearest = []
    house_coord = facilities['coords']
    for facility in facilities['neighbors']:
        #print( type(len(a_star_search_euclidean(map, house_coord, facility[1]))))
        sth = len(a_star_search_euclidean(map, house_coord, facility[1]))
        facility[3] = sth

print_building_dit(buildings_dict)