from numpy import *
import retworkx as rx
from collections import defaultdict
import pydot
import tempfile
import os
from PIL import Image
from pydot import Dot
from retworkx.retworkx import EdgeList


def convert(m: ndarray) -> defaultdict:
    adj: defaultdict = defaultdict(list)
    for k in range(len(m)):
        for j in range(len(m[k])):
            if m[k][j] == 1:
                adj[k].append(j)
    return adj


G: rx.PyGraph = rx.generators.grid_graph(5, 5, None)

dot: Dot = pydot.graph_from_dot_data(G.to_dot())[0]

# plotting retworkx not working finding an alternative method
"""
with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image
"""

M: ndarray = rx.graph_adjacency_matrix(G, None)
AdjList: defaultdict = convert(M)

a: EdgeList = G.edge_list()
with tempfile.NamedTemporaryFile('wt') as fd:
    path: str = fd.name
    for i in a:
        fd.write(str(i[0]) + ' ' + str(i[1]) + '\n')
    fd.flush()
    H: rx.PyGraph = rx.PyGraph()
    H.read_edge_list(path)

"""
dot = pydot.graph_from_dot_data(H.to_dot())[0]

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image
"""
