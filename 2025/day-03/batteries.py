# Code for day 3 of AoC 2025
# Created: 2025-12-03 by Joseph Hall

def part_1(input_data):
    total_joltage = 0

    # Find the index of the maximum in the input row up to -1th
    for row in input_data:
        row_max = max(row[:-1])
        for vind, val in enumerate(row):
            if val == row_max:
                # Check for second digit
                second_digit = max(row[vind+1:])
                
                # Combine digits and add to total joltage
                total_joltage += int(f"{row_max}{second_digit}")
                break
    
    print("Part 1 soln:", total_joltage)
    return


def part_2(input_data):
    # It is as I feared, I must use recursion
    def find_max_digit(row, digits_remaining, current_digits=""):
        if digits_remaining == len(row):
            ret_num = int(f"{current_digits}{(" ".join([str(x) for x in row]).replace(" ", ""))}")
            print(ret_num)
            return ret_num
        
        # Repeat logic for finding the max of the row from part 1
        row_max = max(row[:-(digits_remaining-1)]) if digits_remaining != 1 else max(row)
        print(row, row_max)
        for vind, val in enumerate(row):
            if val == row_max:
                new_digits = f"{current_digits}{row_max}"
                # print(new_digits)
                if digits_remaining == 1:
                    print(new_digits, len(new_digits))
                    return int(new_digits)
                else:
                    return find_max_digit(row[vind+1:], digits_remaining-1, new_digits)
                
    part_2_sol = sum([find_max_digit(x, 12) for x in input_data])
    print("Part 2 solution:", part_2_sol)

    return


def main(input_path="2025/day-03/input-03.txt"):
    # Load the input data
    with open(input_path, "r") as f:
        input_data = f.readlines()

    input_data = [[int(x) for x in y[:-1]] for y in input_data]
    part_1(input_data)
    part_2(input_data)
    return


if __name__ == "__main__":
    main()