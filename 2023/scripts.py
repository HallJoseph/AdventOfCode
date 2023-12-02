import re
import sys


def load_input(path):
    with open(path) as f:
        text = f.read()
    row_list = text.split("\n")
    return row_list


def day_one():
    row_list = load_input("inputs/day_one.txt")

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


def day_two():
    row_list = load_input("inputs/day_two.txt")
    maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    tot = 0
    tot_games = 0
    for game in row_list:
        game_possible = True
        tot_games += 1
        for game_round in game.split(";"):
            for colour in maxes.keys():
                nums_col = re.findall(f'[0-9]* {colour}', game_round)
                if len(nums_col) == 0:
                    continue
                col_tot = int(nums_col[0].split(' ')[0])
                if col_tot > maxes[colour]:
                    game_possible = False
                    break

            if not game_possible:
                break

        if game_possible:
            tot += int(game.split(':')[0].split(' ')[-1])

    print(tot)

    tot2 = 0

    for game in row_list:
        mins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        prod = 1

        for colour in mins.keys():
            nums_col = re.findall(f'[0-9]* {colour}', game)
            col_tot = [int(x.split(' ')[0]) for x in nums_col]
            prod *= max(col_tot)

        tot2 += prod

    print(tot2)
    pass


def main(func_num):
    funcs = {
        1: day_one,
        2: day_two
    }
    funcs[int(func_num)]()


if __name__ == "__main__":
    main(sys.argv[1])
