# Code for AoC 2025 day 8
# Created: 2025-12-08, by Joseph Hall

import numpy as np
import pandas as pd
import tqdm
import networkx as nx

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
    dists_df = dists_df[["starts", "ends", "dists"]]
    
    # Find k shortest dists
    k = 1000
    shortest_dists = dists_df[:k]
    shortest_dists = shortest_dists
    edges_arr = shortest_dists.values
    print(edges_arr)
    
    # Use shortest dists to build graph
    G = nx.Graph()
    G.add_nodes_from([x for x in range(input_size)])
    G.add_weighted_edges_from(edges_arr)
    
    # Find the sizes of each of the networks
    network_sizes = [len(x) for x in nx.connected_components(G)]
    network_sizes.sort(reverse=True)
    print(network_sizes)

    # Solution is the product of the first n values in network sizes
    n=3
    print("Part 1 sol:", np.prod(network_sizes[:n]))

    # Part 2 solution -- coding here rather than separate function
    other_edges = dists_df[k:].values
    for edge in other_edges:
        G.add_weighted_edges_from([edge])
        if len(list(nx.connected_components(G))) == 1:
            final_x1 = input_data[int(edge[0]), 0]
            final_x2 = input_data[int(edge[1]), 0]

            print("Part 2 sol:", final_x1 * final_x2)
            break

    return


def part_2(input_data):
    return


def main(input_path="2025/day-08/input-08.txt"):
    input_data = np.loadtxt(input_path, delimiter=",")
    part_1(input_data)
    return


if __name__ == "__main__":
    main()