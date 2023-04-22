"""Day 1"""

def part_1():
    file = open("input.txt", "r")
    data = [int(line.strip()) for line in file.readlines()]
    result = get_increasing_measurements(data)
    print(result)

def get_increasing_measurements(measurements):
    """Return the number of measurements that are bigger than the previous."""
    increasing_measurements = 0
    for index, measure in enumerate(measurements):
        if index == 0:
            continue
        if measure > measurements[index-1]:
            increasing_measurements += 1
    return increasing_measurements

part_1()