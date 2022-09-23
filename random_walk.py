## Implementation of RWR algorithm for part 5
import itertools

import networkx as nx
import numpy as np
from scipy.linalg import inv
from scipy.sparse import coo_matrix

from graph_methods import add_edges, add_nodes


def rwr(g):
    # Create adjacency matrix from human protein interaction network
    network = read_network()
    matrix = nx.adjacency_matrix(network)
    create_diagonal(matrix)


    pass

def read_network():
    '''
    Helper function to read full human network file and create graph.
    '''
    human_network = nx.MultiDiGraph()

    f = open("PathLinker-results/pathlinker-human-network.txt", "r")
    firstline = f.readline() # Read first line
    assert(firstline[:5] == "#tail") # Check that correct table is being read

    for line in f:
        arr = line.split()
        assert(len(arr) > 2) # first two columns relevant

        # Create and add edge - use arr values
        human_network.add_edge(arr[0], arr[1]) # tail to head

    f.close()

    return human_network

def create_diagonal(A):
    '''
    Helper function to create diagonal matrix.
    '''
    coo = coo_matrix(A)

    for i in zip(coo.row):
        sum = 0
        for j in zip(coo.col):

            if i != j:
                sum += coo[i][j]