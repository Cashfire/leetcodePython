"""
given a list of positive integers representing the amounts of time those queries take to execute.
Only one query can be executed at a time, but they can be executed in any order.
A query's waiting time is the amount of time that it must wait before its execution starts.
for [1,4,5], the queries' waiting time are 0, 1, 5 respectively, and total 6.
If you execute them as [5,4,1], then waiting time will be 14 = 0+5+9
"""


def minimum_waiting_time(queries):
    # O(nlogn)time and O(1)
    queries.sort()
    total_waiting = 0
    for i, t in enumerate(queries):
        n_query_left = len(queries) - (i+1)
        total_waiting += n_query_left * t
    return total_waiting


if __name__ == "__main__":
    tasks = [3,2,1,2,6]
    print(minimum_waiting_time(tasks))
    print(tasks)
