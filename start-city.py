def validStartingCity(distances, fuel, mpg):
    # O(n^2) time and O(1) space
    n = len(distances)
    for start in range(n):
        fuel_meter = 0
        for j in range(start, start+ n):
            curr = j% n
            fuel_meter += fuel[curr] * mpg - distances[curr]
            if fuel_meter < 0:
                break

        if fuel_meter == 0:
            return start
    return -1


def valid_Starting_City(distances, fuel, mpg):
    # O(n) time and O(1) space
    start_id = 0
    min_fuel = 0
    fuel_state = 0
    for i in range(len(distances)):
        fuel_state += fuel[i] * mpg - distances[i]
        if fuel_state < min_fuel:
            min_fuel = fuel_state
            start_id = i+1
    return start_id


if __name__ == "__main__":
    distances1 = [5, 25, 15, 10, 15]
    fuel1 = [1, 2, 1, 0, 3]
    mpg1 = 10
    print(validStartingCity(distances1, fuel1, mpg1))
    print(-1//2)
