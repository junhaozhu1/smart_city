import math
INIT_TIME_WALK = 2
INIT_TIME_BIKE = 3
INIT_TIME_CAR = 5

# 计算两点之间的欧式距离
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def add_to_buildings(buildings):
    buildings_dict = {}

    for building_id, coords in buildings:
        if building_id[:2] == 'Re':
            buildings_dict[building_id] = {'coords': coords, 'neighbors': []}

    for building_id, coords in buildings:
        if building_id[:2] != 'Re':
            for house_id, house_info in buildings_dict.items():
                distance = euclidean_distance(coords, house_info['coords'])
                astar = 0
                access = {"walk": INIT_TIME_WALK, "bike": INIT_TIME_BIKE, "drive": INIT_TIME_CAR}
                house_info['neighbors'].append([building_id, coords, distance, astar, access])

    for house_id, house_info in buildings_dict.items():
        house_info['neighbors'] = sorted(house_info['neighbors'], key=lambda x: x[2])
    return buildings_dict

def print_building_dit(buildings_dict):
    for house_id, house_info in buildings_dict.items():
        print(f"House ID: {house_id}")
        print(f"  Coordinates: {house_info['coords']}")
        print("  Neighbors:")
        for neighbor_info in house_info['neighbors']:
            print(f"    {neighbor_info[0]} - Coordinates: {neighbor_info[1]}, Absolute Distance: {neighbor_info[2]}"
                  f", Actual Distance: {neighbor_info[3]}")
