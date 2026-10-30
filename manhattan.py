import heapq

# Define the target goal configuration
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# Heuristic 2: Manhattan Distance calculation
def heuristic(state):
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            goal_pos = tile - 1
            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_pos, 3)
            distance += abs(row1 - row2) + abs(col1 - col2)
    return distance

# Generate valid next moves by shifting the empty space (0)
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            s = state[:]
            s[zero], s[new_pos] = s[new_pos], s[zero] # Swap tiles
            neighbors.append(s)
    return neighbors

# A* Search algorithm implementation
def astar(start):
    # Priority queue stores tuples of: (f(n), g(n), state)
    pq = [(heuristic(start), 0, start)]
    visited = set()
    
    while pq:
        f, g, state = heapq.heappop(pq)
        
        if state == goal:
            print("Goal reached!")
            return
            
        key = tuple(state)
        if key in visited:
            continue
        visited.add(key)
        
        # Print exploration path details
        print("State:", state, "g =", g, "h =", heuristic(state), "f =", f)
        
        for next_state in get_neighbors(state):
            if tuple(next_state) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state)
                heapq.heappush(pq, (new_f, new_g, next_state))

# Initial starting state
start = [2, 8, 3, 
         1, 6, 4, 
         7, 0, 5]

# Execute the search
astar(start)
