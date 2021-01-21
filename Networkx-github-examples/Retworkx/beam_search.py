import math
import matplotlib.pyplot as plt
import retworkx as rx
import networkx as nx
import numpy
from typing import *

def progressive_widening_search(G, source, value, condition, initial_width=1)->int :
    if condition(source):
        return source
    log_m=math.ceil(math.log2((len(G1))))
    for i in range(log_m):
        width=initial_width*pow(2,i)
        for u, v in nx.bfs_beam_edges(G1, source, value, width):
            if condition(v):
                return v
    print(nx.NodeNotFound("no node"))

def has_high_centrality(v:int) -> bool:
    return centrality[v] >= avg_centrality

seed: int = 89

#conversion of retworkx graph to networkx couldnt find any func in retworkx to calculate centality
G: rx.PyGraph =rx.undirected_gnp_random_graph(100,0.5,seed=seed)
n1 : numpy.ndarray = rx.graph_adjacency_matrix(G, None)
G1:nx.classes.graph.Graph = nx.from_numpy_matrix(n1)


centrality: dict =nx.eigenvector_centrality(G1)
avg_centrality:float = sum(centrality.values()) / len(G1)

source: int =0
value=centrality.get
condition: bool =has_high_centrality
found_node:int =progressive_widening_search(G1,source,value,condition)
c:float =centrality[found_node]
print(f"found node {found_node} with centrality {c}")

#plotting
pos=nx.spring_layout(G1,seed=seed)
options = {
    "node_color": "blue",
    "node_size": 20,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.1,
}
nx.draw(G1, pos, **options)
nx.draw_networkx_nodes(G1, pos, nodelist=[found_node], node_size=100, node_color="r")
plt.show()
