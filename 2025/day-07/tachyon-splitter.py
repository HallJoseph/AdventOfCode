# Code for AoC 2025 Day 7
# Created: 2025-12-07, by Joseph Hall

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LogNorm

def animate(frames):
    fig, ax = plt.subplots()
    div = make_axes_locatable(ax)
    cax = div.append_axes('right', '5%', '5%')
    
    init_frame = frames[0]
    im = ax.imshow(init_frame, origin='lower', norm=LogNorm(), cmap="inferno") # Here make an AxesImage rather than contour
    cb = fig.colorbar(im, cax=cax)
    tx = ax.set_title('Level 0')

    def animate_loc(i):
        arr = frames[i]
        vmax     = np.max(arr)
        vmin     = np.min(arr)
        im.set_data(arr)
        im.set_clim(vmin, vmax)
        tx.set_text(f'Level {i}')

    ani = animation.FuncAnimation(fig, animate_loc, frames=len(frames), interval=100,
                                    repeat_delay=5000)
    # ani = animation.ArtistAnimation(fig, ims)

    writer = animation.FFMpegWriter(
        fps=15, metadata=dict(artist='Me'), bitrate=1800)
    
    ani.save("2025/day-07/part-2-visual.gif", writer=writer)
    plt.show()


def part_1(input_data):
    beams = input_data[0] == "S"
    print(beams)
    tot_splits = 0
    for row in input_data:
        splitters = row == "^"
        beams_to_split = splitters & beams
        # print(beams_to_split)
        split_inds = beams_to_split.nonzero()[0]
        row_splits = len(split_inds)

        # Split to the left
        new_left_inds = split_inds - 1
        new_left_inds = new_left_inds[new_left_inds >= 0]  # deal with edge cases
        new_left = np.zeros_like(row, dtype=int)
        new_left[new_left_inds] += 1

        # Split right
        new_right_inds = split_inds + 1
        new_right_inds = new_right_inds[new_right_inds <= len(row)]  # deal with edge cases
        new_right = np.zeros_like(row, dtype=int)
        new_right[new_right_inds] += 1

        new_beams = (new_left | new_right | beams) & ~splitters
        #print(new_beams)
        row_vis = row.copy()
        row_vis[new_beams.nonzero()[0]] = "|"

        # row_splits = np.sum(new_beams) - np.sum(beams)
        tot_splits += row_splits
        beams = new_beams.copy()


    print("Part 1 sol:", tot_splits)
    return


def part_2(input_data):
    # Create a matrix to store number of timelines each splitter produces
    cache_matrix = np.ones_like(input_data, dtype=int)
    vis_arrs = [cache_matrix.copy()]
    # Work from bottom up
    input_data_flip = input_data[::-1].copy()
    for rind, row in enumerate(input_data_flip):
        split_inds = (row == "^").nonzero()[0]

        # Split to the left
        new_left_inds = split_inds - 1
        new_left_inds = new_left_inds[new_left_inds >= 0]  # deal with edge cases
        new_left = np.zeros_like(row, dtype=int)
        new_left[new_left_inds] += 1

        # Split right
        new_right_inds = split_inds + 1
        new_right_inds = new_right_inds[new_right_inds <= len(row)]  # deal with edge cases
        new_right = np.zeros_like(row, dtype=int)
        new_right[new_right_inds] += 1
        
        cache_matrix[rind:, split_inds] = cache_matrix[rind, new_left_inds] + cache_matrix[rind, new_right_inds]
        vis_arrs.append(cache_matrix.copy())

    # Print solution as last value at position corresponding to S in last row of cache matrix
    print("Part 2 solution:", cache_matrix[-1][input_data[0]=="S"])
    animate(vis_arrs)
    return


def main(input_path="2025/day-07/input-07.txt"):
    # Load the data
    input_data = np.loadtxt(input_path, dtype=str)
    input_arr = np.array([list(x) for x in input_data])
    part_1(input_arr)
    part_2(input_arr)
    return


if __name__ == "__main__":
    main()