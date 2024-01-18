hii i am changing something heeeerwgdere
"y": y,
        "r": r,
        "connected_gears": [],
    }

ddef connect_gears(gear1, gear2):
    gear1["connected_gears"].append(gear2)
    gear2["connected_gears"].append(gear1)

def is_valid_gear_chain(gear1, gearN, gears):
    visited = set()
    queue = [gear1]

    while queue:
        current_gear = queue.pop(0)

        if current_gear is gearN:
            return True

        if current_gear in visited:
            return False

        visited.add(current_gear)

        for connected_gear in current_gear["connected_gears"]:
            if len(connected_gear["connected_gears"]) < 2 or len(connected_gear["connected_gears"]) > 3:
                return False

            queue.append(connected_gear)

    return False

def calculate_gear_rotations(gear1, gearN):
    if gear1["x"] == gearN["x"] and gear1["y"] == gearN["y"]:
        return 1

    if not is_valid_gear_chain(gear1, gearN, gears):
        return "Could Not Process"

    gear_rotations = 1
    current_gear = gear1

    while current_gear != gearN:
        next_gear = None

        for connected_gear in current_gear["connected_gears"]:
            if connected_gear != current_gear and connected_gear != gearN:
                next_gear = connected_gear
                break

        if next_gear is None:
            return "Could Not Process"

        gear_rotations *= (next_gear["r"] / current_gear["r"])
        current_gear = next_gear

    return gear_rotations

def main():
    n = int(input())
    gears = []

    for _ in range(n):
        x, y, r = map(int, input().split())
        gear = get_gear_connection((x, y, r))
        gears.append(gear)

    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                continue

            connect_gears(gears[i], gears[j])

    gear1 = gears[0]
    gearN = gears[n - 1]

    gear_rotations = calculate_gear_rotations(gear1, gearN)
    print(gear_rotations)

if __name__ == "__main__":
    main()
