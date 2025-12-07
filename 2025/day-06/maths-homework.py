# Code for AoC 2025 day 6
# Created: 2025-12-06, by Joseph Hall

import numpy as np


def part_1(numbers, operations):
    running_tot = 0
    for row, op in zip(numbers, operations):
        if op == "+":
            running_tot += np.sum(row)
        else:
            running_tot += np.prod(row)
    
    print("Part 1 sol:", running_tot)

    return


def part_2(input_data):
    return


def main(input_path="2025/day-06/input-06.txt"):
    # parse the input
    with open(input_path, "r") as f:
        input_data = f.readlines()
    input_data_change = [x[:-1].split(" ") for x in input_data]
    input_data_final = [[]]*len(input_data_change)
    print(len(input_data_change))
    print(input_data_final)
    for rind, row in enumerate(input_data_change):
        input_data_final[rind] = [x for x in row if (x != "" and x != "\n")]

    numbers = np.array(input_data_final[:-1], dtype=int).transpose()
    operations = input_data_final[-1]
    part_1(numbers, operations)
    return


if __name__ == "__main__":
    main()