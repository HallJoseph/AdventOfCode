import numpy as np
import tqdm


def bubbly_sorty(arr):
    """
    Terrible attempt to implement a bubble sort
    :param arr: Input array to be sorted
    :return: The sorted array
    """
    arr_sorted = arr.copy()
    n_it = 0
    counter = 1

    # Iterate until the list is sorted
    while counter != len(arr_sorted):
        counter = 1
        for ind, value in enumerate(arr_sorted[1:]):
            if value < arr_sorted[ind]:
                arr_sorted[ind], arr_sorted[ind+1] = arr_sorted[ind+1], arr_sorted[ind]
                # Subtract 1 each time the list needs to be resorted
                counter -= 1
            else:
                counter += 1
        n_it += 1
    print(n_it)

    return arr_sorted


def distance_calculator(data_path):
    # Load the data
    inp_data = np.loadtxt(data_path).transpose()

    # Get the two columns and sort them
    col_a = bubbly_sorty(inp_data[0])
    col_b = bubbly_sorty(inp_data[1])

    # Get the absolute differences between the elements in the list
    dists = np.abs(col_a - col_b)

    # Sum the distances to get the total distances
    total_distance = np.sum(dists)
    print(total_distance)


def similarity_calculator(data_path):
    # Load the data
    inp_data = np.loadtxt(data_path).transpose()

    # Get the two columns and sort them
    col_a = inp_data[0]
    col_b = inp_data[1]

    # Iterate over col A, count how many times it appears in col B and do multiply-addy stuff
    total = 0
    for x in tqdm.tqdm(col_a):
        count_b = np.sum(col_b == x)
        total += x * count_b

    print(total)


if __name__ == '__main__':
    similarity_calculator('input-01.txt')
