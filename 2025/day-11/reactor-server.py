# Code AoC 2025 day 10
# Created: 2025-12-04, by Joseph Hall

import networkx as nx
from multiprocessing import Pool


def count_paths(inpt):
    graph, start, end = inpt
    return len(list(nx.all_simple_paths(graph, start, end)))


def part_1(input_data):
    # Parse the input data
    nodes = " ".join(input_data).replace(":", "").split(" ")
    nodes_unique = list(set(nodes))
    
    # Make the graph
    G = nx.DiGraph()
    G.add_nodes_from(nodes_unique)

    # Add edges
    for node_conns in input_data:
        split_conns = node_conns.split(":")
        in_node, out_nodes = split_conns[0].strip(), split_conns[1].strip().split(" ")
        edges_to_add = [(in_node, x) for x in out_nodes]
        G.add_edges_from(edges_to_add)

    # # Get the number of paths
    # n_paths = nx.all_simple_paths(G, "you", "out")
    # print("Part 1 sol:", len(list(n_paths)))

    # PART 2 logic, graph too big to just do same thing again
    #   n_paths = nx.all_simple_paths(G, "svr", "out")

    # instead, let's try evaluating all paths svr --> fft, svr --> dac, dac <--> fft, dac --> out, fft --> out
    #   hmm, that's still slow with the full data...

    # okay.... good news is that there are 0 paths dac --> fft, but many fft --> dac
    #   means we can evaluate svr --> fft * fft --> dac * dac --> out
    #   still slow, maybe just need to be patient
    #       orrrr MP these bitches
    pool = Pool()
    returns = pool.map(
        count_paths,
        [
            (G, "svr", "fft"),
            (G, "fft", "dac"),
            (G, "dac", "out")
        ]
    )
    routes = returns[0] * returns[1] * returns[2]
    print("Part 2 sol:", routes)
    return


def part_2(input_data):
    return


def main(input_path="2025/day-11/input-11.txt"):
    with open(input_path, "r") as f:
        input_data = f.readlines()
    input_data = [x[:-1] for x in input_data]
    part_1(input_data)
    return


if __name__ == "__main__":
    main()
