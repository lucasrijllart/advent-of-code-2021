"""Day 1"""

def part_1(file_name):
    """Return the number of measurements that are in increasing order."""
    import os
    a= os.listdir('.')
    file = open(file_name, "r")
    data = [int(line.strip()) for line in file.readlines()]  # parsing
    return get_increasing_measurements(data)


def get_increasing_measurements(measurements):
    """Return the number of measurements that are bigger than the previous."""
    increasing_measurements = 0
    for index, measure in enumerate(measurements):
        if index == 0:
            continue
        if measure > measurements[index-1]:
            increasing_measurements += 1
    return increasing_measurements

if __name__ == "__main__":
    part_1_result = part_1("input.txt")
    print("Part 1:", part_1_result)