
class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.__graph__ = dict()
        else:
            self.__graph__ = graph_dict

    def neighbors(self, n):
        return self.__graph__.get(n)

    def add_edge(self, n1, n2, weight=0):
        self.__graph__.setdefault(n1,{})
        self.__graph__.get(n1)[n2] = weight
        self.__graph__.setdefault(n2,{})
        self.__graph__.get(n2)[n1] = weight

    def del_edge(self, n1, n2):
        n1_dict = self.__graph__.get(n1)
        if n1_dict is None:
            return
        n1_n2_dict = n1_dict.get(n2)
        if n1_n2_dict is None:
            return
        else:
            del(self.__graph__[n1][n2])
            del(self.__graph__[n2][n1])
            if len(n1_dict) == 0:
                del(self.__graph__[n1])
            if len(self.__graph__[n2]) == 0:
                del(self.__graph__[n2])

    def __str__(self):
        return str(self.__graph__)



if __name__ == "__main__":
    graph_dict1 = {'A': {'B': 1, 'C':2},
                'B':{'A':1, 'D':3},
                'C':{'A':2},
                'D':{'B':3}}
    my_graph1 = Graph(graph_dict1)

    # my_graph1.del_edge('D',"B")

    print(my_graph1.neighbors('E'))
