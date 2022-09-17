## Main code for Assignment 1
# Andy Athawale

import networkx as nx
import matplotlib.pyplot as plt

from graph_methods import *

g = nx.MultiDiGraph()
add_edges(g, "NetPath-pathways/EGFR1-edges.txt")
print(g)