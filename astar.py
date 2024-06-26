import pandas as pd
import math
import heapq


# Adjusted Euclidean heuristic to support diagonal movement
def euclidean_heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Modified A* search to include diagonal neighbors
def a_star_search_euclidean(map, start, goal):
    rows, cols = len(map), len(map[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: euclidean_heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        neighbors = [
            (current[0] + dx, current[1] + dy)
            for dx in range(-1, 2)  # Allows diagonal movement
            for dy in range(-1, 2)  # Allows diagonal movement
            if (dx != 0 or dy != 0) and 0 <= current[0] + dx < rows and 0 <= current[1] + dy < cols
        ]

        for neighbor in neighbors:
            if map[neighbor[0]][neighbor[1]] == '#' or neighbor in g_score:
                continue

            tentative_g_score = g_score[current] + euclidean_heuristic(current, neighbor)
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euclidean_heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))


    return []

# def astar_calc():
#     # Run the A* search with the adjusted Euclidean heuristic for the start and all end points
#     euclidean_paths = []
#     for end in ends:
#         path = a_star_search_euclidean(map, start, end)
#         if path:
#             euclidean_paths.append(path)
#
#     shortest_euclidean_path = min(euclidean_paths, key=len)
#     shortest_path_end = shortest_euclidean_path[len(shortest_euclidean_path)-1]
#
#     print("Shortest Path:", shortest_euclidean_path)  # Displaying the shortest path found using the adjusted Euclidean method.
#     print("End Coordinates:", shortest_path_end)