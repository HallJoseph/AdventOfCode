# Day 2 code for AoC
# Created 2025-12-01 by Joseph Hall

def part_1(input_list):
    invalid_tot = 0
    
    # Iterate over the ID ranges
    for id_range in input_list:
        lo_hi = id_range.split('-')
        lo_id, hi_id = int(lo_hi[0]), int(lo_hi[1])

        # Iterate over IDs in this range
        for test_id in range(lo_id, hi_id+1):
            test_string = str(test_id)
            test_length = len(test_string)

            # Skip ID if an odd number of digits
            if (test_length % 2) != 0:
                continue
            
            # Check if first half of ID is same as second half
            if test_string[:int(test_length/2)] == test_string[int(test_length/2):]:
                invalid_tot += test_id

    print("Part 1 soln: ", invalid_tot)
    return


def part_2():
    return


def main(input_path="2025/day-02/input-02.txt"):
    with open(input_path, "r") as f:
        input_data = f.read()
    input_list = input_data.split(",")
    
    part_1(input_list)
    return


if __name__ == "__main__":
    main()