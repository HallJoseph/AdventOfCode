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


def path_count(current, end, conn_dict, cache={}):
    # Function with caching for trying to faster find number of paths between two nodes
    #   Adapted from @DariusMichienzi's day 11 code in julia

    # Check if at the end of the chain, and return 1 (i.e. 1 path to get there foun)
    if current == end:
        return 1
    
    # Check if the number of paths between current and end needs to be found
    if (current, end) not in cache.keys():
        # Find the number of available paths with the holy power of recursion
        paths = 0

        # Split on if looking for the output or looking for another node (to allow escape
        #   if reaching end of graph without finding a valid path)
        if end == "out":
            paths = sum([path_count(conn, end, conn_dict, cache) for conn in conn_dict[current]])

        else:
            # Iterate over connections and reject if output: this allows 0 paths to be found
            for conn in conn_dict[current]:
                if conn != "out":
                    paths += path_count(conn, end, conn_dict, cache)

        # Update the connections dictionary with the number of paths we've found
        cache[current, end] = paths

    return cache[current, end]


def part_2(input_data):
    # Redoing part 2 here, but with my own (read: adapted from Darius' code) cached search
    #   function which should hopefully be a bit faster than the one from networkx

    # Parse the input data into a dictionary
    conn_dict = {}
    for node_conn in input_data:
        node_split = node_conn.split(":")
        conn_dict[node_split[0]] = node_split[1].strip().split(" ")

    # Find the paths by multiplying svr --> ftt, fft --> dac, and dac --> out (Might need MPing)
    paths = path_count("svr", "fft", conn_dict) * path_count("fft", "dac", conn_dict) * path_count("dac", "out", conn_dict)
    print("Part 2 sol:", paths)
    return


def main(input_path="2025/day-11/input-11.txt"):
    with open(input_path, "r") as f:
        input_data = f.readlines()
    input_data = [x[:-1] for x in input_data]

    part_2(input_data)
    return


if __name__ == "__main__":
    main()
