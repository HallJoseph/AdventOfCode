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
    return


def main(input_path="2025/day-03/input-03.txt"):
    # Load the input data
    with open(input_path, "r") as f:
        input_data = f.readlines()

    input_data = [[int(x) for x in y[:-1]] for y in input_data]
    part_1(input_data)
    return


if __name__ == "__main__":
    main()