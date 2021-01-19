import os
import tempfile
from PIL import Image
import pydot
#import networkx as nx
import retworkx as rx
import igraph as ig
import numpy as np

G = rx.undirected_gnm_random_graph(1000, 2000,None)

components = rx.strongly_connected_components(G)

largest_component = max(components, key=len)
H = G.subgraph(largest_component)


dot = pydot.graph_from_dot_data(G.to_dot())[0]
with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image

n1 = rx.graph_adjacency_matrix(G, None)

g = ig.Graph.Weighted_Adjacency(n1.tolist())
ig.plot(g)
