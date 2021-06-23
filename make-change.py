def min_coins_for_change(t, denoms):
    # O(t) time and O(t) space
    # num_coins[i] represents the min coins required to make $i
    num_coins = [float('inf')] * (t+1)
    num_coins[0] = 0  # 0 coins are required to make $0
    for d in denoms:
        for i in range(1, t+1):
            if d <= i:
                num_coins[i] = min(num_coins[i], num_coins[i - d] + 1)
    return num_coins[t] if num_coins[t] != float('inf') else -1


def ways_make_change(t, denoms):
    # O(t) time and O(t) space
    # ways[i] represents the max ways to make $i
    ways = [0 for i in range(t + 1)]
    ways[0] = 1  # only 1 way to make $0, i.e. use no coin
    for d in denoms:
        for i in range(1, t+1):
            if d <= i:
                ways[i] += ways[i - d]
    return ways[t]


if __name__ == "__main__":
    arr1 = [2,3]
    ways_make_change(6, arr1)
    print(min_coins_for_change(6, arr1))
    print(min_coins_for_change(7, [2,4]))
