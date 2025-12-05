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

    ranges = input_data.copy()
    prev_ranges = ranges.copy() + 1
    update_done = True
    print(ranges.transpose())
    n_iter = 0
    while np.sum(np.abs(ranges - prev_ranges)) != 0:
        n_iter += 1
        prev_ranges = ranges.copy()
        new_ranges = np.zeros_like(ranges)
        for lind, lims in enumerate(ranges.transpose()):
            # Mask where low ends less than current low end
            lo_mins_mask = ranges[0] <= lims[0]
            # Mask where hi ends greater than current
            lo_maxs_mask = ranges[1] >= lims[0]
            # Combine for new lows
            new_lo_mask = lo_mins_mask & lo_maxs_mask
            print(new_lo_mask)

            # Mask where low ends less than current high end
            hi_mins_mask = ranges[0] <= lims[1]
            # Mask where hi ends greater than current
            hi_maxs_mask = ranges[1] >= lims[1]
            # Combine for new lows
            new_hi_mask = hi_mins_mask & hi_maxs_mask
            #print(new_hi_mask)

            # Update the ranges
            new_lo = min(ranges[0][new_lo_mask])
            print(lims[0], new_lo)
            new_hi = max(ranges[1][new_hi_mask])
            print(lims[1], new_hi)
            new_ranges[0, lind] = new_lo
            new_ranges[1, lind] = new_hi
        
        print(new_ranges.transpose())
        ranges = new_ranges.copy()
            
        
    print(len(ranges.transpose()))
    print(n_iter)

    # remove duplicates
    final_lims = [[], []]
    for lims in ranges.transpose():
        if lims[0] not in final_lims[0]:
            final_lims[0].append(lims[0])
            final_lims[1].append(lims[1])
    
    print(np.transpose(final_lims))
    # Find diff between high and low
    lims_arr = np.array(final_lims)
    lims_diff = lims_arr[1] - lims_arr[0]
    # Plus lims diff to deal with off by one errs
    total_ids = np.sum(lims_diff) + len(lims_diff)

    print("Part 2 solution:", total_ids)
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
    import time
    ts = time.time()
    part_2(range_lims_arr)
    print("time takens (s)", time.time() - ts)
    
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