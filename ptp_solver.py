from student_utils import *
import networkx as nx
import itertools

flag = False

def total_distance(tour, length, H, alpha):
    
    drive_cost = alpha * sum(length[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    walk_cost = sum(length[min(tour, key=lambda x: length[x][home])][home] for home in H)
    total_cost = drive_cost + walk_cost
    return total_cost

def is_connected_tour(tour, G):
    G_copy = G.copy()
    G_copy = G_copy.to_undirected()
    remove_nodes = G.nodes - set(tour)
    if remove_nodes:
        for element in remove_nodes:
            G_copy.remove_node(element)
    return nx.is_connected(G_copy)

def ptp_solver(G:nx.Graph, H:list, alpha:float):
    """
    PTP solver.
    Input:
        G: a NetworkX graph representing the city.
        H: a list of home nodes that you must visit.
        alpha: the coefficient of calculating cost.
    Output:
        tour: a list of nodes traversed by your car.
        pick_up_locs_dict: a dictionary of (pick-up-locations, friends-picked-up) pairs
        where friends-picked-up is a list/tuple containing friends who get picked up at
        that specific pick-up location. Friends are represented by their home nodes.

    All nodes are represented as integers.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph.
    Pick-up locations must be in the tour.
    Everyone should get picked up exactly once.
    """
    
    length = dict(nx.all_pairs_dijkstra_path_length(G)) 
    path_dict = dict(nx.all_pairs_dijkstra_path(G))
    
    global flag
    visit = []
    cur_node = 0
    visit.append(0)
    while len(set(visit) & set(H)) < len(H):
        mini = float('inf')
        temp = None
        home_left = list(filter(lambda home: home not in visit, H))
        for i in home_left:
            if mini > length[cur_node][i]:
                mini = length[cur_node][i]
                temp = i
        visit.extend(path_dict[cur_node][temp][1:])
        cur_node = temp

    if cur_node != 0:
        visit.extend(path_dict[cur_node][0][1:])
    tour = visit
    distance = total_distance(tour, length, H, alpha)
    cur_tour = tour

    while True:
        flag = False
        for index in range(1, len(tour) - 1):
        
            if tour[index-1] != tour[index+1]:
                connect = path_dict[tour[index-1]][tour[index+1]][1:-1]
                temp_tour = tour[:index] + connect + tour[index+1:]
            else:
                temp_tour = tour[:index-1] + tour[index+1:]

    
            temp = total_distance(temp_tour, length, H, alpha)

            if temp < distance:
                flag = True
                cur_tour, distance = temp_tour, temp
                    
        for vertex in G.nodes:
            if vertex not in tour:
                for index in range(1, len(tour) - 1):
                    connect1 = path_dict[tour[index-1]][vertex][1:]
                    connect2 = path_dict[vertex][tour[index+1]][1:-1]
                    connect = connect1 + connect2
                    temp_tour = tour[:index] + connect + tour[index:]
                
                    temp = total_distance(temp_tour, length, H, alpha)

                    if temp < distance:
                        flag = True
                        cur_tour, distance = temp_tour, temp

        tour = cur_tour
        if not flag:
            break

    norm_tour = [tour[0]]
    for i in range(1, len(tour)):
        if tour[i] != tour[i-1]:
            norm_tour.append(tour[i]) 
    
    tour = norm_tour
    pick_up_locs_dict = {}
    for home in H:
        pickup_loc = min(tour, key=lambda tour_node: length[tour_node][home])
        if pickup_loc in pick_up_locs_dict:
            pick_up_locs_dict[pickup_loc].append(home)
        else:
            pick_up_locs_dict[pickup_loc] = [home]

    return tour, pick_up_locs_dict


if __name__ == "__main__":
    pass




