import re
import sys


def day_one():
    with open("inputs/day_one.txt") as f:
        text = f.read()
    row_list = text.split("\n")
    print(row_list)

    # Part one
    tot = 0
    for item in row_list:
        nums = re.findall("[0-9]", item)
        tot += int(f"{nums[0]}{nums[-1]}")
    print(tot)

    # Part 2
    written_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def convert_to_int(num):
        try:
            return int(num)
        except:
            return written_to_num[num]

    tot2 = 0
    pattern = "|".join(
        written_to_num.keys()
    )
    pattern += '|["0-9"]'
    print(pattern)
    for item in row_list:
        nums = re.findall(pattern, item)
        num1 = convert_to_int(nums[0])
        num2 = convert_to_int(nums[-1])
        tot2 += int(f"{num1}{num2}")
    print(tot2)


def main(func_num):
    funcs = {
        1: day_one
    }
    funcs[int(func_num)]()


if __name__ == "__main__":
    main(sys.argv[1])
