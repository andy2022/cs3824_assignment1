# Function to compute shortest path from each source to each target.
import networkx as nx
from precision_recall import generate

def func(g):
    '''
    For the given graph, finds edges of the shortest path between two
    specified nodes (source to target). Uses networkx Djikstra
    implementation, which returns list of nodes including source and target.
    g: Graph to run Djikstra algorithm
    '''
    assert(g.number_of_nodes() != 0) # Ensure graph is not empty

    # Get source nodes list from the graph
    sources = [n for n,v in g.nodes(data=True) if v["node_type"] == "receptor"]

    # Store all paths lists in a separate list
    paths = []

    # Iterate through all source nodes, apply Dijkstra algorithm
    for each in sources:
        length, path = nx.single_source_dijkstra(g, each)

        targets = [x for x,y in g.nodes(data=True) if y['node_type'] == 'tf']
        for target in targets:

            # If a target node was found in the shortest paths
            if target in length.keys():
                paths.append(path[target])

    # Rank all paths - sorting method by length
    paths.sort(key=len)

    # Separate all paths into individual edges - store in edges dict
    edges = {}
    for each in paths:

        key = len(each)

        # If path list size is not 2, separate into individual edges
        if len(each) > 2:
            for i in range(len(each)-1):
                if not key in edges.keys():
                    edges[key] = [each[i:i+2]]
                else:
                    edges[key].append(each[i:i+2])
        else:
            if not key in edges.keys():
                    edges[key] = [each]
            else:
                edges[key].append(each)

    # Return edges dict
    return edges

