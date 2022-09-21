## Main code for Assignment 1
# Andy Athawale

import networkx as nx
import matplotlib.pyplot as plt

from graph_methods import *
from parsing import parse
from precision_recall import func

# Part 1 - construct 4 graphs
egfr = nx.MultiDiGraph()
tgf_beta = nx.MultiDiGraph()
tnf_alpha = nx.MultiDiGraph()
wnt = nx.MultiDiGraph()
# Add all nodes & edges
add_nodes(egfr, "NetPath-pathways/EGFR1-nodes.txt")
add_edges(egfr, "NetPath-pathways/EGFR1-edges.txt")
add_nodes(tgf_beta, "NetPath-pathways/TGF_beta_Receptor-nodes.txt")
add_edges(tgf_beta, "NetPath-pathways/TGF_beta_Receptor-edges.txt")
add_nodes(tnf_alpha, "NetPath-pathways/TNFalpha-nodes.txt")
add_edges(tnf_alpha, "NetPath-pathways/TNFalpha-edges.txt")
add_nodes(wnt, "NetPath-pathways/Wnt-nodes.txt")
add_edges(wnt, "NetPath-pathways/Wnt-edges.txt")

# Part 2 - parsing ranked edges
egfr_rankededges = parse("PathLinker-results/EGFR1-k_20000-ranked-edges.txt")
tgf_beta_rankededges = parse("PathLinker-results/TGF_beta_Receptor-k_20000-ranked-edges.txt")
tnf_alpha_rankededges = parse("PathLinker-results/TNFalpha-k_20000-ranked-edges.txt")
wnt_rankededges = parse("PathLinker-results/Wnt-k_20000-ranked-edges.txt")

# Part 3 - precision-recall curves
precision, recall = func(egfr_rankededges, egfr)
print("S")