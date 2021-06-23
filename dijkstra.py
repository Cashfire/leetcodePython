import heapq

def dijkstrasAlgorithm(start, edges):
    dist_list = [-1 for i in range(len(edges))]
    frontier_heap = [(0, start)]
    visited = set()
    while frontier_heap:
        parent_dist, parent_idx = heapq.heappop(frontier_heap)
        # print("poped: (", parent_idx, ', dist=', parent_dist)
        if parent_idx in visited:
            continue
        visited.add(parent_dist)
        if dist_list[parent_idx] == -1:
            dist_list[parent_idx] = parent_dist
        for child in edges[parent_idx]:
            child_idx, child_cost = child
            if child_idx not in visited:
                total_dist = parent_dist + child_cost
                heapq.heappush(frontier_heap, (total_dist, child_idx))
                # print("added: (", child_idx, ', cost=', total_dist)
    return dist_list


if __name__ == "__main__":
    ans1 = [0, 7, 13, 27, 10, -1]
    edges1 = [
        [[1, 7]],
        [[2, 6],[3, 20],[4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        []]
    start1 = 0
    print(dijkstrasAlgorithm(start1, edges1) == ans1)
    print(dijkstrasAlgorithm(start1, edges1))
