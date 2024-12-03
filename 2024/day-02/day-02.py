import numpy as np


def check_safety(test_line):
    # Actually perform the safety checks, first check if all descending or all ascending
    diffs = test_line[:-1] - test_line[1:]
    if not (np.all((diffs > 0)) or np.all(diffs < 0)):
        return 0

    # Now check magnitude of difference, just need to check if absolute is <= 3 because have already eliminated cases of
    #   0 difference
    abs_diffs = np.abs(diffs)
    if np.all((abs_diffs <= 3)):
        return 1
    else:
        return 0


def safety_checks(input_path):
    # Load the input data
    with open(input_path) as f:
        input_data = f.readlines()

    # Convert the input data to a list of numpy arrays
    data_arrays = [np.array([int(y) for y in x[:-1].split(' ')]) for x in input_data]

    n_safe = 0
    # Iterate over the arrays
    for line in data_arrays:
        # Check the safety
        n_safe += check_safety(line)

    print(n_safe)

if __name__ == '__main__':
    safety_checks('input-02.txt')
