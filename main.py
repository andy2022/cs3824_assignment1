## Main code for Assignment 1
# Andy Athawale

import networkx as nx
import matplotlib.pyplot as plt

from graph_methods import *
from parsing import parse
from precision_recall import generate
from shortest_path import func
from random_walk import rwr

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

'''
# Part 3 - precision-recall curves
egfr_precision, egfr_recall = generate(egfr_rankededges, egfr)
tgf_precision, tgf_recall = generate(tgf_beta_rankededges, tgf_beta)
tnf_precision, tnf_recall = generate(tnf_alpha_rankededges, tnf_alpha)
wnt_precision, wnt_recall = generate(wnt_rankededges, wnt)
plt.plot(egfr_recall, egfr_precision, "g", label="EGFR")
plt.plot(tgf_recall, tgf_precision, "r", label="TGF Beta")
plt.plot(tnf_recall, tnf_precision, "b", label = "TNF Alpha")
plt.plot(wnt_recall, wnt_precision, "k", label = "Wnt")
plt.xlim(0, 0.2)
plt.legend()
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.savefig("pt3.png")
plt.clf()

# Part 4 - shortest path algorithm
shortest_egfr_edges = func(egfr)
shortest_egfr_precision, shortest_egfr_recall = generate(shortest_egfr_edges, egfr)
shortest_tgf_edges = func(tgf_beta)
shortest_tgf_precision, shortest_tgf_recall = generate(shortest_tgf_edges, tgf_beta)
shortest_tnf_edges = func(tnf_alpha)
shortest_tnf_precision, shortest_tnf_recall = generate(shortest_tnf_edges, tnf_alpha)
shortest_wnt_edges = func(wnt)
shortest_wnt_precision, shortest_wnt_recall = generate(shortest_wnt_edges, wnt)
plt.plot(shortest_egfr_recall, shortest_egfr_precision, "g", label="EGFR")
plt.plot(shortest_tgf_recall, shortest_tgf_precision, "r", label="TGF Beta")
plt.plot(shortest_tnf_recall, shortest_tnf_precision, "b", label = "TNF Alpha")
plt.plot(shortest_wnt_recall, shortest_wnt_precision, "k", label = "Wnt")
plt.legend()
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.savefig("shortest.png")
plt.clf()
'''

# Part 5 - RWR algorithm
rwr(egfr)
print("S")