# Basic code structure for AoC 2025
# Created: 2025-12-04, by Joseph Hall

import numpy as np


def part_1(input_data):
    # Find all rolls
    roll_mask = input_data.nonzero()
    print(roll_mask)
    
    # Define a 3x3 mask
    total_accessible = 0
    # For each roll, count adjacent rolls
    for roll_x, roll_y in zip(roll_mask[0], roll_mask[1]):
        adjacent_sector = (input_data[roll_x-1:roll_x+2, roll_y-1:roll_y+2])
        if np.sum(adjacent_sector) <= 4:
            total_accessible += 1
    print(total_accessible)
    return


def part_2(input_data):
    return


def main(input_path="2025/day-04/input-04.txt"):
    # Parse the input
    with open(input_path, "r") as f:
        input_lines = f.readlines()
    
    input_lines = [[0] + list(x[:-1].replace("@", "1").replace(".", "0")) + [0] for x in input_lines]
    print(np.shape(input_lines))
    input_data = np.zeros((len(input_lines) + 2, len(input_lines[0])), dtype="int")
    
    input_data[1:-1] = input_lines
    part_1(input_data)
    return


if __name__ == "__main__":
    main()