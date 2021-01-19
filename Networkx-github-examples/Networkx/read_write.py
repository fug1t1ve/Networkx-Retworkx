import matplotlib.pyplot as plt
import networkx as nx

G = nx.grid_2d_graph(5, 5)  # 5x5 grid

for line in nx.generate_adjlist(G):
    print(line)
nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

pos = nx.spring_layout(H, seed=200)
nx.draw(H, pos)
plt.show()
