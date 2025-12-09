# Code for AoC 2025 day 9, copied part 1 logic from day 8
# Created: 2025-12-09, by Joseph Hall

import numpy as np
import pandas as pd
import tqdm

def part_1(input_data):
    # Find distances between all pairs of nodes
    input_size = len(input_data)
    dists = []
    starts = []
    ends = []
    for nind, node in enumerate(tqdm.tqdm(input_data)):
        node_dists = np.sqrt(np.sum((input_data[nind+1:] - node)**2, axis=1)).tolist()
        node_starts = [nind] * (input_size-(nind+1))
        node_ends = [x for x in range(nind+1, input_size)]
        
        dists += node_dists
        starts += node_starts
        ends += node_ends
    
    # Convert to dataframe
    dists_df = pd.DataFrame.from_records(
        {
            "starts": starts,
            "ends": ends,
            "dists": dists
        }
    ).sort_values(by="dists")

    return


def main(input_path="2025/day-09/input-09.txt"):
    input_data = np.loadtxt(input_path, delimiter=",")
    part_1(input_data)
    return


if __name__ == "__main__":
    main()
