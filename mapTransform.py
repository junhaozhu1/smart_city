import math
from drawroad import drawRoad

def map_transform(residents, facilities, roads):
    # get city size
    x_max = -1
    y_max = -1

    if roads:
        for road in roads:
            if (road.start[0] or road.end[0]) > x_max:
                x_max = max(road.start[0], road.end[0])
            if (road.start[1] or road.end[1]) > y_max:
                y_max = max(road.start[1], road.end[1])

    if residents:
        for facility in residents:
            if facility.location[0] > x_max:
                x_max = facility.location[0]
            if facility.location[1] > y_max:
                y_max = facility.location[1]

    if facilities:
        for facility in facilities:
            if facility.location[0] > x_max:
                x_max = facility.location[0]
            if facility.location[1] > y_max:
                y_max = facility.location[1]

    x_max = int(x_max) + 1
    y_max = int(y_max) + 1

    map = drawRoad(y_max, x_max, roads)

    map = map_inverse(map, x_max, y_max)

    return map


def map_inverse(map, x, y):
    ix = 0
    while ix < x:
        iy = 0
        while iy < y:
            if map[ix][iy] is None:
                map[ix][iy] = '#'
            if map[ix][iy] == '#':
                map[ix][iy] = None
            iy += 1
        ix += 1
    return map

def create_grid(rows, cols, default_value=None):
    grid = [[default_value for _ in range(cols)] for _ in range(rows)]
    return grid

# x1 = math.ceil(int(x1))
# x2 = math.ceil(int(x2))
# y1 = math.ceil(int(y1))
# y2 = math.ceil(int(y2))

def print_map(grid):
    for row in grid:
        for item in row:
            if item is None:
                print("{:<5}".format(""), end="")
            elif item == "#":
                print("{:<5}".format("#"), end="")
            else:
                print("{:<5}".format(item), end="")
        print()