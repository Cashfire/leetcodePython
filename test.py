from grah import Graph
import sys
int_inf = sys.maxsize


def IDS(start, goal, graph):
    explored_set = set()
    for depth in range(int_inf):
        result = DLS(start, goal, graph, explored_set, depth)
        if result:
            return True
    return result


def DLS(start, goal, graph, explored, depth):
    verbose = True
    if verbose:
        indent = " " * (2-depth) * 2
        print(indent,"DLS(",start, ",",goal,"depth=",depth,")")
    if start == goal:
        return True
    elif depth == 0:
        return False
    explored.add(start)
    children = graph.neighbors(start)
    if children is None:
        return
    result = None
    for child,_ in children.items():
        if child in explored:
            continue
        result = DLS(child, goal, graph, explored, depth-1)
        if result:
            return result
    return result

if __name__ == "__main__":
    print("In DLS")
    graph_dict1 = {'A': {'B': 1, 'C':2},
                'B':{'A':1, 'D':3, 'E':3},
                'C':{'A':2, 'F':5, 'G':4},
                'D':{'B':3},
                'E':{'B':3},
                'F':{'C':5},
                'G':{'C':4}}
    my_graph1 = Graph(graph_dict1)
    # print(DLS('A','E',my_graph1, set(), 2))
    # print(DLS('A','G',my_graph1, set(), 2))
    print(IDS('A','E',my_graph1))
