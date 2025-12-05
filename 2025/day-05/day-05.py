# Day 5 code
# Created: 2025-12-05, by Joseph Hall


import tqdm
import numpy as np


def part_1(ranges, ids):
    n_fresh = 0
    for id in ids:
        id_test = int(id)
        # Mask to get ranges for the id
        print((id))
        id_mask_lo = ranges[0] <= id_test
        id_mask_hi = ranges[1] >= id_test

        # Combine the masks, if any true left over then in range
        combine_mask = id_mask_lo & id_mask_hi
        if sum(combine_mask) != 0:
            n_fresh += 1
    print("Part 1 solution:", n_fresh)
    return


def part_2(input_data):
    # We want to find all the overlapping ranges, I have an idea for how to do this using my solution 
    # for part 1 but not sure if it will work

    
    return


def main(input_path="2025/day-05/input-05.txt"):
    # Massage the input
    with open(input_path, "r") as f:
        input_data = f.read()

    input_split = input_data.split("\n\n")
    ranges, ids = input_split[0].split("\n"), input_split[1].split("\n")[:-1]
    print(ranges)
    print(ids)

    # Let's use a 2D array to describe this
    range_lims_arr = np.zeros((2, len(ranges)))
    for rind, rang in enumerate(ranges):
        range_lims = rang.split("-")
        range_lims_arr[0, rind], range_lims_arr[1, rind] = int(range_lims[0]), int(range_lims[1])
    print(range_lims_arr)

    part_1(range_lims_arr, ids)
    part_2(range_lims_arr)
    
    # Process ranges DON'T DO THIS IT EATS RAM
    #full_ranges = []
    #for rang in tqdm.tqdm(ranges):
    #    range_lims = rang.split("-")
    #    range_lo, range_hi = int(range_lims[0]), int(range_lims[1]) + 1
    #    full_ranges += [x for x in range(range_lo, range_hi)]
    #

    return


if __name__ == "__main__":
    main()