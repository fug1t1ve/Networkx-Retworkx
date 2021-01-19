import retworkx as rx
from collections import defaultdict
import pydot
import tempfile
import os
from PIL import Image

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList

G=rx.generators.grid_graph(5,5,None)

dot = pydot.graph_from_dot_data(G.to_dot())[0]

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image


M=rx.graph_adjacency_matrix(G,None)
AdjList = convert(M)

print(AdjList)

a=G.edge_list()

H=rx.PyGraph()
H.read_edge_list(a)

dot = pydot.graph_from_dot_data(H.to_dot())[0]

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = os.path.join(tmpdirname, 'dag.png')
    dot.write_png(tmp_path)
    image = Image.open(tmp_path)
    os.remove(tmp_path)
image

