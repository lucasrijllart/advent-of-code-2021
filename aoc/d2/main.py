"""Day 2"""

def part_1(file_name):
    """Return the distance and depth multiplied by each other."""
    data = parse_input(file_name)
    distance, depth = get_distance_and_depth(data)
    return distance * depth

def part_2(file_name):
    """Not used yet"""

def parse_input(file_name: str) -> list:
    """Return a list of tuples with the first character of the direction and the value.
    Example: forwards 5 -> [("f", 5)]
    """
    data = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            line = line.strip()
            data.append((line[0], int(line[-1])))
    return data

def get_distance_and_depth(data):
    """Return two values: distance and depth. Distance is affected by forwards movement.
    Depth is affected by up and down movement.
    """
    distance, depth = 0, 0
    for entry in data:
        direction, value = entry[0], entry[1]
        if direction == "f":  # forwards
            distance += value
        else:
            if direction == "d":  # down
                depth += value
            elif direction == "u":  # up
                depth -= value
    return distance, depth

if __name__ == "__main__":
    file_name = "input.txt"
    part_1_result = part_1(file_name)
    print("Part 1:", part_1_result)
    part_2_result = part_2(file_name)
    print("Part 2:", part_2_result)