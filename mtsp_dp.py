import networkx as nx

def mtsp_dp(G):
    """
    TSP solver using dynamic programming.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the problem using dynamic programming.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in G exactly once.
    """
    memory = {}
    def dp(temp_vertex, temp_nodes):
        if len(temp_nodes) == 0:
            memory[(temp_vertex,tuple(temp_nodes))] = G.edges[0,temp_vertex]['weight']
            return memory[(temp_vertex,tuple(temp_nodes))]
        elif (temp_vertex, tuple(temp_nodes)) in memory.keys():
            return memory[(temp_vertex,tuple(temp_nodes))]
        else:
            min = float('inf')
            for before_vertex in temp_nodes:
                after_noeds = temp_nodes
                after_noeds.remove(before_vertex)
                temp_path = dp(before_vertex, after_noeds) + G.edges[before_vertex, temp_vertex]['weight']
                if min > temp_path:
                    min = temp_path
            memory[(temp_vertex,tuple(temp_nodes))] = min
            return memory[(temp_vertex,tuple(temp_nodes))]
    tour = [0]
    Nodes = sorted(G.nodes())
    t_Nodes = Nodes.copy()
    t_Nodes.remove(0)
    l_vertex = 0
    while(len(t_Nodes) > 0):
        minimum = float('inf')
        for vertex in t_Nodes:
            pass_path = t_Nodes.copy()
            pass_path.remove(vertex)
            t_value = G.edges[vertex, l_vertex]['weight'] + dp(vertex, pass_path)
            
            if minimum > t_value:
                minimum = t_value
                now_vertex = vertex
        tour.append(now_vertex)
        t_Nodes.remove(now_vertex)
        l_vertex = now_vertex
    tour.append(0)
    tour.reverse()
    return tour

'''G = nx.Graph()
e_list = [(0,1,2),(0,2,2),(0,3,2),(0,4,2),
            (1,2,2 ),(1,3,3),(1,4,4),
            (2,3,2),(2,4,3),
            (3,4,2)]
G.add_weighted_edges_from(e_list)
print(mtsp_dp(G))'''



