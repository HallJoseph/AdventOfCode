# Code for AoC 2025 day 9, copied part 1 logic from day 8
# Created: 2025-12-09, by Joseph Hall

import numpy as np
import pandas as pd
import tqdm
import matplotlib.pyplot as plt

def part_1(input_data):
    # Find distances between all pairs of nodes
    input_size = len(input_data)
    areas = []
    starts = []
    ends = []
    for nind, node in enumerate(tqdm.tqdm(input_data)):
        other_tiles = input_data[nind+1:].transpose()
        rect_areas = (np.abs(1+node[0] - other_tiles[0]) * np.abs(1+node[1] - other_tiles[1])).tolist()
        rect_starts = [nind] * (input_size-(nind+1))
        rect_ends = list(range(nind+1, input_size))
        
        areas += rect_areas
        starts += rect_starts
        ends += rect_ends
    
    # Convert to dataframe
    areas_df = pd.DataFrame.from_records(
        {
            "starts": starts,
            "ends": ends,
            "areas": areas
        }
    ).sort_values(by="areas", ascending=False)

    print("Part 1 sol:", areas_df["areas"].values[0])
    return part_2(input_data, areas_df)


def part_2(input_data, areas_df):
    # Transpose the input
    input_transpose = input_data.transpose()

    # Offset the input coords to minimise grid size (minor but should work
    red_tile_coords = np.array([input_transpose[0]-np.min(input_transpose[0]), input_transpose[1]-np.min(input_transpose[1])], dtype=int)
    red_tiles_indiv = red_tile_coords.transpose()
    
    # Define our gird based on the red_tile_coords
    tile_grid = np.zeros((np.max(red_tile_coords[0])+1, np.max(red_tile_coords[1])+1)).transpose()
    print(tile_grid.shape)

    # Mark red tiles
    tile_grid[red_tile_coords] = 1
    print("Red tiles marked")

    # Mark connecting green tiles
    for rind, red_tile in red_tiles_indiv:
        next_tile = red_tiles_indiv[rind] + 1
        diff = next_tile - red_tile

        # Find which axis to set as green tiles
        zero_index = (diff == 0).nonzero[0]
        print(zero_index)
        return


def main(input_path="2025/day-09/input-09.txt"):
    input_data = np.loadtxt(input_path, delimiter=",")
    part_1(input_data)
    return


if __name__ == "__main__":
    main()
