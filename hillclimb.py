# Calculate the number of conflicting pairs of queens (heuristic cost)
def cost(state):
    h = 0
    for i in range(4):
        for j in range(i + 1, 4):
            # Check if queens share the same row or the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

# Display the 4x4 board layout visually
def print_board(state):
    for i in range(4):
        for j in range(4):
            if state[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Hill Climbing optimization algorithm
def hill_climbing():
    current = [3, 1, 2, 0]  # Initial state configuration
    print("Initial State:", current)
    print("Cost:", cost(current))
    print_board(current)
    
    while cost(current) != 0:
        neighbors = []
        # Generate all successor states by swapping queen positions
        for i in range(4):
            for j in range(i + 1, 4):
                neighbor = current.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append((cost(neighbor), i, j, neighbor))
                
        # Find the neighbor with the lowest heuristic cost
        best = min(neighbors)
        
        # If no neighbor improves the cost, we stop (Local Optimum)
        if best[0] >= cost(current):
            print("Local optimum reached.")
            break
            
        current = best[3]
        print("Current State:", current)
        print("Cost:", cost(current))
        print_board(current)
        
    if cost(current) == 0:
        print("Goal State:", current)
        print("Final Cost:", cost(current))

# Execute the algorithm
hill_climbing()
