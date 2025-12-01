# Day 1 code for AoC
# Created 2025-12-01 by Joseph Hall


def part_1(input_path="2025/day-01/input-01.txt"):

    with open(input_path, "r") as f:
        pass_code = f.readlines()

    tot = 50
    pwd = 0
    for line in pass_code:
        # Extract number of clicks
        n_clicks = int(line[1:-1])
        # Pass direction
        if line[0].upper() == "L":
            tot -= n_clicks
        else:
            tot += n_clicks

        # Check to see if at 0
        if (tot % 100) == 0:
            pwd += 1
        print(tot)
    
    print(pwd)
    return


def part_2(input_path="2025/day-01/input-01.txt"):

    with open(input_path, "r") as f:
        pass_code = f.readlines()

    tot = 50
    pwd = 0
    for line in pass_code:
        # Extract number of clicks
        n_clicks = int(line[1:-1])

        # This is a terrible solution, but yeet
        positive = line[0].upper() == "R"
        for click in range(n_clicks):
            tot = tot + 1 if positive else tot - 1
            # Check to see if at 0
            if (tot % 100) == 0:
                pwd += 1
    
    print("part 2 password:", pwd)
    return


def main(input_path="2025/day-01/input-01.txt"):
    part_1(input_path)
    part_2(input_path)


if __name__ == "__main__":
    main()