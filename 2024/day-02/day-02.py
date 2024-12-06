import numpy
import numpy as np


def check_safety(test_line):
    # print()
    copy_line = test_line.copy()
    # Actually perform the safety checks, first check if all descending or all ascending
    diffs = test_line[:-1] - test_line[1:]
    removed_elems = 0
    safe = 0
    removed = False
    if not (np.all((diffs > 0)) or np.all(diffs < 0)):
        for ind in range(len(copy_line)):
            rm_line = numpy.append(copy_line[:ind], copy_line[ind+1:])
            rm_diffs = rm_line[:-1] - rm_line[1:]
            print(rm_line, rm_diffs, rm_line[0] - rm_line[1])

            if np.all((rm_diffs > 0)) != np.all(rm_diffs < 0):
                print(f'safe when removing {ind}', np.all((rm_diffs > 0)), np.all(rm_diffs < 0))
                safe += 1
                copy_line_2 = rm_line.copy()
                diffs = rm_diffs
                removed = True
                break

        if safe != 1:
            # print(copy_line)
            return 0
    else:
        copy_line_2 = copy_line.copy()

    # Now check magnitude of difference, just need to check if absolute is <= 3 because have already eliminated cases of
    #   0 difference
    abs_diffs = np.abs(diffs)
    if np.all((abs_diffs <= 3)):
        return 1
    elif not removed:
        for ind in range(len(copy_line_2)):
            rm_line = numpy.append(copy_line_2[:ind], copy_line_2[ind+1:])
            print(rm_line)
            rm_diffs = rm_line[:-1] - rm_line[1:]
            rm_abs_diffs = np.abs(rm_diffs)
            if np.all((rm_abs_diffs <= 3)):
                safe += 1
                return 1

        return 0
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
    safety_checks('test-input-02.txt')
