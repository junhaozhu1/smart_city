import math

def add_line_to_map(map, start, end):
    # Bresenham 算法绘制直线
    y0, x0 = start
    y1, x1 = end

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
        map[y0][x0] = '#'
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    map[y0][x0] = '#'  # 添加终点

def drawRoad(rows, cols, roads):

    # 创建一个 10x10 的地图
    map = [['.' for _ in range(cols)] for _ in range(rows)]

    # add structures
    if roads:
        for facility in roads:
            add_line_to_map(map, facility.start, facility.end)
            for structure in facility.depending_facilities:
                print(map[int(structure[1][0])][int(structure[1][1])])
                map[int(structure[1][0])][int(structure[1][1])] = structure[0]

    return map