import heapq

def is_valid_move(pos, graph):
    n_row, n_col = get_graph_row_col(graph)
    pos0, pos1 = pos
    valid_row = 0 <= pos0 < n_row
    valid_col = 0 <= pos1 < n_col
    return valid_row and valid_col


def get_graph_row_col(graph):
    return len(graph), len(graph[0])


def get_children(node, graph):
    # node = (curr_cost, removed_wall_n, curr_position)
    # not allow diagonal moves, only allows [left, right, up, down]
    result = []
    n_row, n_col = get_graph_row_col(graph)
    curr_cost, removed_wall_n, curr_position = node
    removed_wall_imit = 1
    delta = [(0,1), (0,-1), (1,0), (-1, 0)]
    for i in delta:
        new_position = curr_position[0] + i[0], curr_position[1] + i[1]
        if is_valid_move(new_position, graph):
            r = new_position[0]
            c = new_position[1]
            new_value = graph[new_position[0]][new_position[1]]
            if removed_wall_n == removed_wall_imit and new_value == 1:
                continue
            new_node = (curr_cost + 1, removed_wall_n + new_value, new_position)
            result.append(new_node)
    return result

# if just return #steps, no need to use ancestor_dict
# if return path, use ancestor_dict to keep track positions
def ucs(graph):
    start = (0,0)
    n_row = len(graph)
    n_col = len(graph[0])
    goal = (n_row - 1, n_col - 1)
    frontier_pq = [(1, 0, start)]
    explored_set = set()

    while len(frontier_pq) > 0:
        parent_node = heapq.heappop(frontier_pq)
        parent_cost, wall_n, parent_position = parent_node
        # print('pop parent=',parent_position, 'cost=',parent_cost)
        if parent_position == goal:
            return parent_cost
        explored_set.add(parent_position)
        for child_node in get_children(parent_node, graph):
            if child_node[2] not in explored_set:
                # heuristic_cost = goal[0] - child[0] + goal[1] - child[1] - reduced_cost
                heapq.heappush(frontier_pq, child_node)
    return parent_cost


def find_path_usc(graph):
    start = (0,0)
    goal = (len(graph)-1, len(graph[0])-1)
    path_dict = {start: [start]}
    frontier_pq = [(0, 0, start)] #node = (curr_cost, removed_wall_n, curr_position)
    explored = set()
    while len(frontier_pq) > 0 and goal not in explored:
        parent_node = heapq.heappop(frontier_pq)
        parent_cost, parent_removed_wall, parent_pos = parent_node
        # print('pop: ', parent_pos)
        if parent_pos in explored:
            continue
        explored.add(parent_pos)
        children = get_children(parent_node, graph)
        # shorter = get_shorter_path(path_dict, children, parent_node)
        for child_node in children:
            cost, walls_n, pos = child_node
            cost_record = path_dict.get(pos)
            if cost_record is not None and cost >= len(cost_record):
                continue
            heapq.heappush(frontier_pq, child_node)
            path_dict[pos] = path_dict[parent_pos] + [pos]
            # print('push to frontier: ', child_node)
            # print('update path_dict: ', path_dict)

    if goal in explored:
        return path_dict[goal] + [goal]
    else:
        raise ValueError("no path")


def get_shorter_path(paths, neighbors, parent_node):
    # return ((node, [path to its parent]
    parent = parent_node[-1]
    path = paths[parent] + [parent]
    for child in neighbors:
        n = child[-1]
        if n in paths and len(paths[n]) <= len(path):
            print("----- ignored ", n)
            continue
        yield child, path


if __name__ == "__main__":
    # case1 return 7 not 6, the start counts 1
    case1 = [[0, 1, 1, 0],
             [0, 0, 0, 1],
             [1, 1, 0, 0],
             [1, 1, 1, 0]];
    # print(ucs(case1))
    print(find_path_usc(case1))
    # case1 return 11 not 10, the start counts 1
    case2 = [[0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0]]
    # print(ucs(case2))
    # print(get_graph_row_col(case2))
    print(find_path_usc(case2))
