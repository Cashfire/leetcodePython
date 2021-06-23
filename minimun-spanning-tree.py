from collections import defaultdict
from heapq import *


def get_path_prim(graph):
    n = len(graph)
    q = []
    cost = 0
    visited = set()
    result = []
    heappush(q, (0,0))
    for _ in range(n):
        c, node = heappop(q)
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        cost += c
        for neighbor, dist in g[node]:
            if neighbor in visited:
                continue
            heappush(q, (dist, neighbor))
    return cost, result


def find_root(x):
    if x != p[x]:
        p[x] = find_root(p[p[x]])
    return p[x]


def get_path_kruskal(sorted_edges):
    cost = 0
    for n1, n2, c in sorted_edges:
        r1, r2 = find_root(n1), find_root(n2)
        if r1 == r2:
            continue
        p[r1] = r2
        cost += c
    return cost


if __name__ == "__main__":
    print()
    edges = [[0,1,1], [0,2,6], [2,3,2], [1,2,4], [1,3,5], [0,3,3]]  #[n1,n2,dist]
    g = defaultdict(list)
    for e in edges:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2]))
    total_cost, paths = get_path_prim(g)
    print("total_cost=", total_cost)
    print("path: ", paths)
    p = list(range(4))  # initiate every node as itself's root.
    edges2 = sorted(edges, key=lambda x:x[2])

    print(get_path_kruskal(edges2))











