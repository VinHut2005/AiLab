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

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

def display(path):
    if path is None:
        print("No solution found")
        return
    print("Solution found in", len(path) - 1, "moves")
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()

start = (1, 2, 3,
         7, 8, 4,
         6, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

display(dfs(start, goal))
