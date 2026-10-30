def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_zero = r * 3 + c
            temp = list(state)
            temp[zero], temp[new_zero] = temp[new_zero], temp[zero]
            neighbors.append(tuple(temp))
    return neighbors

def depth_limited_search(state, goal, limit, path):
    if state == goal:
        return path
    if limit == 0:
        return None
    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(neighbor, goal, limit - 1, path + [neighbor])
            if result is not None:
                return result
    return None

def ids(start, goal, max_depth=30):
    for depth in range(max_depth + 1):
        result = depth_limited_search(start, goal, depth, [start])
        if result is not None:
            return result
    return None

def display(path):
    if path is None:
        print("No solution found within the depth limit")
        return
    print("Solution found in", len(path) - 1, "moves")
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()

start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

display(ids(start, goal))
