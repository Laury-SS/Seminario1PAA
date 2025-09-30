import os
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(G, pos, filename, title=""):
    plt.figure(figsize=(7, 5))
    nx.draw_networkx_nodes(G, pos, node_color="white", edgecolors="black")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", connectionstyle="arc3,rad=0.08")
    labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()


def draw_augmented_graph(G, pos, filename, title=""):
    plt.figure(figsize=(7, 5))
    nx.draw_networkx_nodes(G, pos, node_color="white", edgecolors="black")
    nx.draw_networkx_labels(G, pos)
    originals = [(u, v) for u, v, d in G.edges(data=True) if not d.get("duplicate", False)]
    duplicates = [(u, v) for u, v, d in G.edges(data=True) if d.get("duplicate", False)]
    nx.draw_networkx_edges(G, pos, edgelist=originals, width=2, edge_color="gray")
    nx.draw_networkx_edges(G, pos, edgelist=duplicates, width=2.5, edge_color="blue", style="dashed")
    labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
