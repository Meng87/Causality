import sys

#PC
sys.path.append("")
import unittest
import numpy as np
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz, chisq, gsq, mv_fisherz, kci

#FCI
import pandas as pd
from causallearn.search.ConstraintBased.FCI import fci, mod_endpoint
from causallearn.utils.cit import fisherz, kci
from itertools import combinations
from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.graph.GraphNode import GraphNode
from causallearn.graph.Edge import Edge
from causallearn.graph.Endpoint import Endpoint
from causallearn.utils.GraphUtils import GraphUtils

#GES
from causallearn.search.ScoreBased.GES import ges

# http://archive.ics.uci.edu/ml/datasets/Abalone

def test_pc_with_fisher_z():
    data_path = "abalone_wsex.txt"
    data = np.loadtxt(data_path, skiprows=1)  # Import the file at data_path as data
    cg = pc(data, 0.05, fisherz, True, 0,
            -1)  # Run PC and obtain the estimated graph (CausalGraph object)

    # visualization using pydot
    # cg.draw_pydot_graph()

    # visualization using networkx
    cg.to_nx_graph()
    cg.draw_nx_graph(skel=False)

    print('finish')

def test_pc_with_kci():
    data_path = "abalone_wsex2.txt"
    data = np.loadtxt(data_path, skiprows=1)[:1000, :]  # Import the file at data_path as data
    cg = pc(data, 0.05, kci, True, 0,
            -1)  # Run PC and obtain the estimated graph (CausalGraph object)

    # visualization using pydot
    # cg.draw_pydot_graph()

    # visualization using networkx
    cg.to_nx_graph()
    cg.draw_nx_graph(skel=False)

    print('finish')

def test_from_txt():
    df = pd.read_csv('abalone_wsex2.txt', delimiter=' ')
    data = df.to_numpy()
    data = data[:1000, :]
    v_labels = df.columns.to_list()

    resultG = fci(data, kci, 0.01, verbose=False)
    resultGnodes = resultG.get_nodes()
    nodes = []
    for v in v_labels:
        nodes.append(GraphNode(v))
    G = GeneralGraph(nodes)

    for x, y in combinations(resultGnodes, 2):
        edge = resultG.get_edge(x, y)
        if edge:
            x = edge.get_node1()
            y = edge.get_node2()
            xend = edge.get_endpoint1()
            yend = edge.get_endpoint2()
            edge = Edge(nodes[resultGnodes.index(x)], nodes[resultGnodes.index(y)], Endpoint.CIRCLE,
                        Endpoint.CIRCLE)
            mod_endpoint(edge, nodes[resultGnodes.index(x)], xend)
            mod_endpoint(edge, nodes[resultGnodes.index(y)], yend)

            print(edge)
            G.add_edge(edge)

    result = str(G)
    print(result)
    with open("result_fcisex.txt", "w") as result_file:
        result_file.write(result)

def test_single_gen():
    X = np.loadtxt(fname='abalone_wsex2.txt',skiprows=1)[:1000, :]
    Record = ges(X, 'local_score_CV_general', maxP=3)
    print(Record["G"])
    print(Record["score"])


# test_pc_with_fisher_z()
# test_pc_with_kci()
# test_from_txt()
test_single_gen()
