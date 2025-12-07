# Code for AoC 2025 Day 7
# Created: 2025-12-07, by Joseph Hall

import numpy as np


def part_1(input_data):
    beams = input_data[0] == "S"
    print(beams)
    tot_splits = 0
    for row in input_data:
        splitters = row == "^"
        beams_to_split = splitters & beams
        # print(beams_to_split)
        split_inds = beams_to_split.nonzero()[0]
        row_splits = len(split_inds)

        # Split to the left
        new_left_inds = split_inds - 1
        new_left_inds = new_left_inds[new_left_inds >= 0]  # deal with edge cases
        new_left = np.zeros_like(row, dtype=int)
        new_left[new_left_inds] += 1

        # Split right
        new_right_inds = split_inds + 1
        new_right_inds = new_right_inds[new_right_inds <= len(row)]  # deal with edge cases
        new_right = np.zeros_like(row, dtype=int)
        new_right[new_right_inds] += 1

        new_beams = (new_left | new_right | beams) & ~splitters
        #print(new_beams)
        row_vis = row.copy()
        row_vis[new_beams.nonzero()[0]] = "|"

        # row_splits = np.sum(new_beams) - np.sum(beams)
        tot_splits += row_splits
        beams = new_beams.copy()


    print("Part 1 sol:", tot_splits)
    return


def part_2(input_data):
    return


def main(input_path="2025/day-07/input-07.txt"):
    # Load the data
    input_data = np.loadtxt(input_path, dtype=str)
    input_arr = np.array([list(x) for x in input_data])
    part_1(input_arr)
    return


if __name__ == "__main__":
    main()