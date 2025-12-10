# AoC day 10 script
# Created: 2025-12-10, by Joseph Hall

import numpy as np
import itertools
import tqdm
from multiprocessing import Pool

def part_1(input_data):
    req_presses = 0

    for row in tqdm.tqdm(input_data):
        # Parse row info
        split_lights = row.split("]")
        lights = split_lights[0][1:]
        inputs_jolts = split_lights[1].split("{")
        inputs = inputs_jolts[0].strip()[1:-1].split(") (")

        # Turn lights into boolean array
        required_lights = np.array([True if x == "#" else False for x in lights], dtype=bool)
        start_lights = np.zeros_like(required_lights, dtype=bool)

        # Turn inputs into a list of tuples of ints
        input_inds = [np.array(tuple(y.replace(',', '')), dtype=int) for y in inputs]

        # Start looping over combinations of n inputs, increasing n each time till valid input found
        n = 1
        solved = False

        while not solved:
            button_perms = list(itertools.permutations(input_inds, n))

            for perm in button_perms:
                # Reset the lights
                current_lights = start_lights.copy()
                for press in perm:
                    # Switch the input at this index
                    current_lights[press] = ~current_lights[press]

                # After pressing all the buttons check if we've matched the desired lights
                if current_lights.tolist() == required_lights.tolist():
                    solved = True
                    req_presses += n
                    break

            n += 1

    print("Part 1 sol:", req_presses)
    return


# Function to multiprocess for part 2
def count_presses_for_2(row):
    # Parse row info
    split_lights = row.split("]")
    inputs_jolts = split_lights[1].split("{")
    inputs = inputs_jolts[0].strip()[1:-1].split(") (")

    # Turn jolts to list of ints
    jolts = np.array([int(x) for x in inputs_jolts[1].strip()[:-1].split(",")])
    start_jolts = np.zeros_like(jolts)

    # Turn inputs into a list of tuples of ints
    input_inds = [np.array(tuple(y.replace(',', '')), dtype=int) for y in inputs]

    # Start looping over combinations of n inputs, increasing n each time till valid input found
    n = min(jolts)
    solved = False

    while not solved:
        button_perms = list(itertools.combinations_with_replacement(input_inds, n))

        for perm in button_perms:
            # Reset the lights
            current_jolts = start_jolts.copy()
            for press in perm:
                # Switch the input at this index
                current_jolts[press] += 1

            # After pressing all the buttons check if we've matched the desired lights
            if current_jolts.tolist() == jolts.tolist():
                solved = True
                return n
        n += 1

    return n


def part_2_brute_force(input_data):
    # DO NOT DO THIS THIS KILLS COMPUTER
    # Going to use similar logic to part 1, but taking joltages and adding instead
    req_presses = 0    
    pool = Pool()
    presses_return = []
    
    for result in tqdm.tqdm(pool.imap_unordered(count_presses_for_2, input_data), total=len(input_data)):
        presses_return.append(result)
    
    print(presses_return)
    print("Part 2 sol:", sum(presses_return))
    return

def part_2(input_data):
    return


def main(input_path="2025/day-10/input-10.txt"):
    with open(input_path, "r") as f:
        input_data = f.readlines()
    
    # part_1(input_data)
    part_2(input_data)
    return


if __name__ == "__main__":
    main()