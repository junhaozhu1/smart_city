import math

def map_transform(residents, facilities, roads):
    # get city size
    x_max = -1
    y_max = -1
    x_min = math.inf
    y_min = math.inf

    if roads:
        for road in roads:
            if road.start[0] or road.end[0] > x_max:
                x_max = max(road.start[0], road.end[0])
            elif road.start[1] or road.end[1] > y_max:
                y_max = max(road.start[1], road.end[1])
            if road.start[0] or road.end[0] < x_min:
                x_min = min(road.start[0], road.end[0])
            elif road.start[1] or road.end[1] < y_min:
                y_min = min(road.start[1], road.end[1])

    if residents:
        for facility in residents:
            if facility.location[0] > x_max:
                x_max = facility.location[0]
            elif facility.location[1] > y_max:
                y_max = facility.location[1]
            if facility.location[0] < x_min:
                x_min = facility.location[0]
            elif facility.location[1] < y_min:
                y_min = facility.location[1]

    if facilities:
        for facility in facilities:
            if facility.location[0] > x_max:
                x_max = facility.location[0]
            elif facility.location[1] > y_max:
                y_max = facility.location[1]
            if facility.location[0] < x_min:
                x_min = facility.location[0]
            elif facility.location[1] < y_min:
                y_min = facility.location[1]

    print(x_max, x_min, y_max, y_min)
    map = create_grid(math.ceil(int(x_max - x_min)), math.ceil(int(y_max - y_min)))
    print(map)


    if residents:
        for facility in residents:
            print(facility.id)

    if facilities:
        for facility in facilities:
            if facility.location[0] > x_max:
                x_max = facility.location[0]
            elif facility.location[1] > y_max:
                y_max = facility.location[1]
            if facility.location[0] < x_min:
                x_min = facility.location[0]
            elif facility.location[1] < y_min:
                y_min = facility.location[1]
    return map

def create_grid(rows, cols, default_value=None):
    print(rows, cols)
    grid = [[default_value for _ in range(cols)] for _ in range(rows)]
    return grid
