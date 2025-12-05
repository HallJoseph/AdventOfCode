# Basic code structure for AoC 2025
# Created: 2025-12-04, by Joseph Hall

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation


def part_1(input_data):
    # Find all rolls
    roll_mask = input_data.nonzero()
    print(len(roll_mask[0]))
    print(roll_mask)
    
    # Define a 3x3 mask
    total_accessible = 0
    to_remove = []
    # For each roll, count adjacent rolls
    for roll_x, roll_y in zip(roll_mask[0], roll_mask[1]):
        adjacent_sector = (input_data[roll_x-1:roll_x+2, roll_y-1:roll_y+2])
        if np.sum(adjacent_sector) <= 4:
            total_accessible += 1
            to_remove.append([roll_x, roll_y])
    # Turn off if doing part 2
    # print("Part 1 solution:", total_accessible)
    return total_accessible, to_remove


def part_2(input_data):
    can_remove = True
    n_removed = 0
    old_inputs = []
    while can_remove:
        n_access, to_remove = part_1(input_data)
        old_inputs.append(input_data.copy())
        if n_access == 0:
            break
        n_removed += n_access
        
        input_data[*np.transpose(to_remove)] = 0

    print("Part 2 solution:", n_removed)
    return old_inputs


def animate(frames):
    fig, ax = plt.subplots()

    ims = []
    for frame in frames:
        im = ax.imshow(frame) # , animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                    repeat_delay=1000)
    writer = animation.FFMpegWriter(
        fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("2025/day-04/part-2-visual.gif", writer=writer)
    plt.show()


def main(input_path="2025/day-04/input-04.txt"):
    # Parse the input
    with open(input_path, "r") as f:
        input_lines = f.readlines()
    
    input_lines = [[0] + list(x[:-1].replace("@", "1").replace(".", "0")) + [0] for x in input_lines]
    print(np.shape(input_lines))
    input_data = np.zeros((len(input_lines) + 2, len(input_lines[0])), dtype="int")
    
    input_data[1:-1] = input_lines
    to_animate = part_2(input_data)
    animate(to_animate)
    return


if __name__ == "__main__":
    main()