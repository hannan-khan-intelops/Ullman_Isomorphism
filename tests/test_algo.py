import networkx as nx
from ullman_algorithm import UllmanAlgorithm
from Graph import Graph


def test_algo():
    # create a directed tree graph.
    tree_1 = Graph()
    tree_1.add_nodes_from([1, 2, 3, 4, 5, 6])
    tree_1.add_edge(1, 2)
    tree_1.add_edge(1, 3)
    tree_1.add_edge(2, 4)
    tree_1.add_edge(2, 5)
    tree_1.add_edge(5, 6)
    tree_2 = tree_1.copy()


    ua = UllmanAlgorithm()
    result = ua.run(tree_1, tree_2)
    print(result)
