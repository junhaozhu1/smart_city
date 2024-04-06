from csv_to_class import csv_to_classes
from mapTransform import map_transform
from mapTransform import print_map
from astar import a_star_search_euclidean
import math
from add_to_building import add_to_buildings, print_building_dit
from report_gengrate import report

CMP = ["Ho", "Po", "Fi"]
WLL = ["Sc", "Ma", "Cl"]
HAP = ["Pa", "In"]
WALK = 6.9 # 69m/min
BIKE = 27.1
CAR = 66.4


# 读取CSV文件
residents = []
roads = []
facilities = []
residents, facilities, roads = csv_to_classes('city_map.csv')


map = map_transform(residents, facilities, roads)

building_list = []
for i,  line in enumerate(map):
    for j, grid in enumerate(line):
        if grid and grid != '.':
            building_list.append((grid, (i,j)))

buildings_dict = {}
buildings_dict = add_to_buildings(building_list)

for houseId, facilities in buildings_dict.items():
    is_nearest = []
    house_coord = facilities['coords']
    for facility in facilities['neighbors']:
        facility[3] = len(a_star_search_euclidean(map, house_coord, facility[1]))

    facilities['neighbors'] = sorted(facilities['neighbors'], key=lambda x: x[3])
    for facility in facilities['neighbors']:
        if facility[0][:2] in is_nearest:
            facilities['neighbors'].remove(facility)
        else:
            is_nearest.append(facility[0][:2])
            facility[4]['walk'] += facility[3] / WALK
            facility[4]['bike'] += facility[3] / BIKE
            facility[4]['drive'] += facility[3] / CAR


report(buildings_dict, residents)