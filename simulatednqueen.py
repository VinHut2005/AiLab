import random
import math

def cost(state):
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_board(state):
    for row in range(1, 9):
        for col in range(8):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()

def simulated_annealing():
    current = [random.randint(1, 8) for _ in range(8)]
    T = 1000
    cooling_rate = 0.99
    step = 1
    
    print("Initial State:", current)
    print("Initial Cost:", cost(current))
    print_board(current)
    
    while T > 0.1:
        if cost(current) == 0:
            break
            
        next_state = current.copy()
        col = random.randint(0, 7)
        row = random.randint(1, 8)
        next_state[col] = row
        
        current_cost = cost(current)
        next_cost = cost(next_state)
        deltaE = current_cost - next_cost
        
        if deltaE > 0:
            current = next_state
            decision = "Accepted (better state)"
        elif random.random() < math.exp(deltaE / T):
            current = next_state
            decision = "Accepted (probability)"
        else:
            decision = "Rejected"
            
        print(f"Step {step}")
        print("Temperature:", round(T, 2))
        print("Neighbour:", next_state)
        print("Neighbour Cost:", next_cost)
        print("Decision:", decision)
        print("Current State:", current)
        print("Current Cost:", cost(current))
        print_board(current)
        
        T *= cooling_rate
        step += 1
        
    print("Final Solution:", current)
    print("Final Cost:", cost(current))
    
    if cost(current) == 0:
        print("Solution Found!")
    else:
        print("Solution not found. Run again.")
        
    print("Final Board:")
    print_board(current)

simulated_annealing()
