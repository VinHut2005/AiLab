def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"

    if status == "Clean":
        if location == "A":
            return "Move Right"
        else:
            return "Move Left"


# Environment
location = "A"
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

print("SIMPLE REFLEX VACUUM CLEANER")
print("-----------------------------")

for step in range(6):
    status = rooms[location]

    print(f"\nLocation : {location}")
    print(f"Status   : {status}")

    action = simple_reflex_agent(location, status)
    print(f"Action   : {action}")

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean.")
        break
