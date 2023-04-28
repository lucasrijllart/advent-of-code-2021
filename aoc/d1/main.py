"""Day 1"""

def part_1(file_name):
    """Return the number of measurements that are in increasing order."""
    data = parse_input(file_name)
    return get_increasing_measurements(data)

def part_2(file_name):
    """Return the number of measurements that are in increasing order."""
    data = parse_input(file_name)
    return get_increasing_sliding_window(data)

def parse_input(file_name: str) -> list:
    """Return a integer list for a given file name. Format must conform to example given."""
    with open(file_name, "r") as file:
        data = [int(line.strip()) for line in file.readlines()]  # parsing
    return data

def get_increasing_measurements(measurements):
    """Return the number of measurements that are bigger than the previous."""
    increasing_measurements = 0
    for index, measure in enumerate(measurements):
        if index == 0:
            continue
        if measure > measurements[index-1]:
            increasing_measurements += 1
    return increasing_measurements

def get_increasing_sliding_window(measurements):
    """Return the number of measurements that are bigger than the previous in a
    three-measurement sliding window."""
    increasing_measurements = 0
    for index, measure in enumerate(measurements[:-3]):
        first_window = measure + measurements[index+1] + measurements[index+2]
        second_window = measurements[index+1] + measurements[index+2] + measurements[index+3]
        if first_window < second_window:
            increasing_measurements += 1
    return increasing_measurements

if __name__ == "__main__":
    file_name = "input.txt"
    part_1_result = part_1(file_name)
    print("Part 1:", part_1_result)
    part_2_result = part_2(file_name)
    print("Part 2:", part_2_result)