import networkx as nx
from mtsp_dp import mtsp_dp
from student_utils import *

def pthp_solver_from_tsp(G, H):
    """
    PTHP sovler via reduction to Euclidean TSP.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
        H: a list of home nodes that you must vist.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the question by first transforming a PTHP\
    problem to a TSP problem. After solving TSP via the dynammic\
    programming algorithm introduced in lectures, construct a solution\
    for the original PTHP problem.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in H.
    """
    
    # reduction
    def transform(G, H):
        H.append(0)
        Nodes = sorted(G.nodes())
        new_G = nx.Graph()
        for f_vertex in H:
            for s_vertex in H:
                temp_Nodes = Nodes.copy()
                temp_Nodes.remove(s_vertex)
                if s_vertex != f_vertex and new_G.has_edge(f_vertex,s_vertex) == False:
                
                    short_path = nx.shortest_path_length(G, f_vertex, s_vertex, weight = 'weight')
                    new_G.add_edge(f_vertex,s_vertex,weight = short_path)
        return new_G
    reduced_graph = transform(G,H)
    tsp_tour = mtsp_dp(reduced_graph)

    # reduction
    tour = [0]
    for i in range(len(tsp_tour) - 1):
        sub_path = nx.shortest_path(G,tsp_tour[i], tsp_tour[i + 1])
        for vertex in sub_path[1:]:
            tour.append(vertex)


    return tour


if __name__ == "__main__":
    pass