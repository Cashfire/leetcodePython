
def apartmentHunting(blocks, reqs):
    # O((n^2)* m) time & O(n) space
    # n = len(blocks), m = len(reqs)
    n = len(blocks)
    dists = [float('-inf') for i in range(n)]
    for i in range(n):
        for req in reqs:
            req_dist = float('inf')
            for j in range(n):
                if blocks[j][req]:
                    req_dist = min(req_dist, abs(i - j))
            dists[i] = max(dists[i], req_dist)
    return arg_min(dists)

def arg_min(arr):
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def apartmentHunting_optimal(blocks, reqs):
    # O(n*m) time and O(n*m) space
    # dists is m*n, m=len(reqs), n=len(blocks)
    dists = list(map(lambda req: get_req_dist(blocks, req), reqs))
    min_dist = float('inf')
    min_idx = 0
    for i in range(len(blocks)):
        total = max([dists[j][i] for j in range(len(reqs))])
        if total < min_dist:
            min_dist = total
            min_idx = i
    return min_idx


def get_req_dist(blocks, req):
    min_idx = float('inf')
    n = len(blocks)
    dists = [n for i in range(n)]
    for i in range(n):
        if blocks[i][req]:
            min_idx = i
        dists[i] = abs(i - min_idx)
    for i in reversed(range(n)):
        if blocks[i][req]:
            min_idx = i
        dists[i] = min(dists[i], abs(i - min_idx))
    return dists

if __name__ == "__main__":
    reqs1 = ['gym', 'store', 'school']
    blocks1 =[
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": True,
            "school": False,
            "store": False
        },
        {
            "gym": True,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": True
        }]
    ans = list(map(lambda req: get_req_dist(blocks1, req), reqs1))
    print(apartmentHunting_optimal(blocks1, reqs1))
