import os
import tempfile
from typing import Sized

from PIL import Image
import pydot
#import networkx as nx
import retworkx as rx
import plot_igraph as ig
import numpy as np

G:rx.PyDiGraph = rx.directed_gnm_random_graph(1000, 2000,None)

components:list = rx.strongly_connected_components(G)

largest_component:Sized = max(components, key=len)

H:rx.PyGraph = G.subgraph(largest_component)

#have to fix pydot error
"""
dot = pydot.graph_from_dot_data(G.to_dot())[0]
with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image
"""
n1:np.ndarray = rx.digraph_adjacency_matrix(G, None)
g = ig.Graph.Weighted_Adjacency(n1.tolist())
ig.plot(g)
