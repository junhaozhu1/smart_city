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
    print(rows, cols)
    grid = [[default_value for _ in range(cols)] for _ in range(rows)]
    return grid

# x1 = math.ceil(int(x1))
# x2 = math.ceil(int(x2))
# y1 = math.ceil(int(y1))
# y2 = math.ceil(int(y2))

def add_line_to_map(map, start, end):
    # Bresenham 算法绘制直线
    x0, y0 = start
    x1, y1 = end

    x1 = math.ceil(int(x1))
    x0 = math.ceil(int(x0))
    y1 = math.ceil(int(y1))
    y0 = math.ceil(int(y0))

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while (x0, y0) != (x1, y1):
        print(x0, y0)
        map[x0][y0] = '#'
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    map[x0][y0] = '#'  # 添加终点

    return map

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