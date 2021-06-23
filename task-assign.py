def taskAssignment(k, tasks):
    # O(nlogn) time and O(n) space
    paired = []
    duration_dict = get_duration_dict(tasks)
    tasks.sort()
    for i in range(k):
        t1_time = tasks[i]
        t1_id = duration_dict.get(t1_time).pop()
        j = len(tasks) - 1 - i
        t2_time = tasks[j]
        t2_id = duration_dict.get(t2_time).pop()
        paired.append([t1_id, t2_id])
    return paired


def get_duration_dict(tasks):
    duration_dict = {}
    for i,duration in enumerate(tasks):
        if duration in duration_dict:
            duration_dict[duration].append(i)
            # duration_dict.get(duration).append(i)
        else:
            duration_dict[duration] = [i]
    return duration_dict


if __name__ == "__main__":

    k1 = 3
    tasks1 = [3, 1, 5, 1, 3, 4]
    print(taskAssignment(k1, tasks1))
