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
    return combine_mask


def part_2(input_data):
    # We want to find all the overlapping ranges, I have an idea for how to do this using my solution
    # for part 1 but not sure if it will work

    # TL;DR for each lim, see if it is in the band of another range and replace it with that limit
    #   i.e. condsider the ranges: 10-14, 16-20 & 12-18. 16 falls in the range 12-18 and we can replace it,
    #       similarly, 18 is in the range 16-20 and can be replaced, lastly 12 is in the range 10-14 and 14 is
    #       in the range of 12-18 so we can update both of those. The updated array is then:
    #       10-14, 12-20 & 10-20. Repeating this process brings 12-->10 and 14-->20 giving three identical
    #       ranges: 10-20, 10-20 & 10-20. We then turn this into one range by droppind duplicates.
    #
    #       When no more overlapping ranges can be found we subtract the high and low ends of each remaining range
    #       to get the Number of IDs and sum
    #
    #       Potential simplification?
    #           If 2 ranges share one limit (e.g. upper) we can replace the other limit with the more extreme (e.g. lower).
    #           In the example above, after updating 10-14 and 10-20 both share 10 so 14-->20 and 12-20 both share 20 so
    #           12-->10.
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