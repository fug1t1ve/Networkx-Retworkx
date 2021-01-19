import math
import matplotlib.pyplot as plt
import retworkx as rx
import networkx as nx

def progressive_widening_search(G, source, value, condition, initial_width=1):
    if condition(source):
        return source
    log_m=math.ceil(math.log2((len(G1))))
    for i in range(log_m):
        width=initial_width*pow(2,i)
        for u, v in nx.bfs_beam_edges(G1, source, value, width):
            if condition(v):
                return v
    return nx.NodeNotFound("no node")

seed=89

G=rx.undirected_gnp_random_graph(100,0.5,seed=seed)
n1 = rx.graph_adjacency_matrix(G, None)
G1 = nx.from_numpy_matrix(n1)
centrality=nx.eigenvector_centrality(G1)
avg_centrality = sum(centrality.values()) / len(G1)

def has_high_centrality(v):
    return centrality[v] >= avg_centrality

source=0
value=centrality.get
condition=has_high_centrality
found_node=progressive_widening_search(G1,source,value,condition)
c=centrality[found_node]
print(f"found node {found_node} with centrality {c}")

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
