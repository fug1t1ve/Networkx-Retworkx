import matplotlib.pyplot as plt
import networkx as nx
import igraph as ig


G = nx.dense_gnm_random_graph(1000, 2000)

components = nx.connected_components(G)
largest_component = max(components, key=len)
H = G.subgraph(largest_component)

nx.draw(H)
plt.show()

g = ig.Graph.from_networkx(G)
