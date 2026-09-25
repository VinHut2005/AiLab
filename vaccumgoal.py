def goal_based_agent(location, rooms):
    # Goal: both rooms should be clean

    if rooms[location] == "Dirty":
        return "Suck"

    if rooms["A"] == "Dirty":
        if location == "A":
            return "Suck"
        else:
            return "Move Left"

    if rooms["B"] == "Dirty":
        if location == "B":
            return "Suck"
        else:
            return "Move Right"

    return "Stop"


# Environment
location = "A"

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

print("GOAL-BASED VACUUM CLEANER")
print("-------------------------")

while True:
    print(f"\nLocation : {location}")
    print(f"Room A   : {rooms['A']}")
    print(f"Room B   : {rooms['B']}")

    action = goal_based_agent(location, rooms)
    print(f"Action   : {action}")

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    elif action == "Stop":
        print("\nGoal achieved: Both rooms are clean!")
        break


