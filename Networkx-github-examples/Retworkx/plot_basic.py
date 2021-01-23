import retworkx as rx
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.core._multiarray_umath import ndarray

G: rx.PyGraph = rx.generators.cycle_graph(20)
n1: np.ndarray = rx.graph_adjacency_matrix(G, None)
G1: nx.classes.graph.Graph = nx.from_numpy_matrix(n1)
pos: dict = nx.spring_layout(G1, dim=3, seed=779)  # have to find a alternative for spring_layout

node_xyz: ndarray = np.array([pos[v] for v in sorted(G1)])
edge_xyz: ndarray = np.array([(pos[u], pos[v]) for u, v in G1.edges()])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(*node_xyz.T, s=100, ec="w")

for x in edge_xyz:
    ax.plot(*x.T, color="tab:gray")


def _format_axes(ax):
    ax.grid(False)
    for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
        dim.set_ticks([])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


_format_axes(ax)
fig.tight_layout()
plt.show()
