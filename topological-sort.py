from collections import defaultdict


def topologicalSort(jobs, deps):
    result = []
    graph = defaultdict(list)
    indegrees = {}
    roots = set(jobs)
    for prereq, nxt in deps:
        indegrees[nxt] = indegrees.get(nxt, 0) + 1
        graph[prereq].append(nxt)
        roots.discard(nxt)
    if not roots:  # cycle detected
        return result
    queue = list(roots)
    while queue:
        root = queue.pop()
        print("poped: ",root)
        # visited.add(root)
        result.append(root)
        for child in graph[root]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)
                print("added: ", child)
    if len(result) != len(jobs):
        return []
    return result

class JobNode():
    def __init__(self, job_id):
        self.idx = job_id
        self.indegree = 0

    def increment_indegree(self):
        self.indegree += 1

    def decrement_indegree(self):
        self.indegree -= 1


if __name__ == "__main__":
    jobs1 = [1,2,3,4]
    deps1 = [[1,2],[1,3], [4,2],[4,3]]
    print(topologicalSort(jobs1, deps1))
