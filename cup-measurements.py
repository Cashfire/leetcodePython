"""
Given a set of cups with only 2 measuring lines (low, high),
and a target mearsuring cup with (2100, 2300)ml, you are asked to write a function to
determine whether those measuring cups can measure the target cup.
input:  [[200,210],[450,465],[800,850]], and [2100, 2300]
output: true
"""

def ambiguousMeasurements(measuringCups, low, high):
    # O(low*high*n) time and O(low*high)
    cache = {}
    result = measure_rec(low, high, measuringCups, cache)
    # for k,v in cache.items():
    #     if v:
    #         print(k)
    return result

def measure_rec(L, H, cups, cache):
	if (L,H) in cache.keys():
		return cache[(L,H)]
	if H < 0 or L> H:
		return False
	can_measure = False
	for cup in cups:
		cup_low, cup_high = cup
		if L <= cup_low and H >= cup_high:
			can_measure = True
			break
		can_measure = measure_rec(L - cup_low, H - cup_high,  cups, cache)
		if can_measure:
			break
	cache[(L,H)] = can_measure
	return can_measure


if __name__ == "__main__":
    measuringCups1 = [[1, 3],[2, 4],[5, 7],[10, 20]]
    low1, high1 = 10, 12
    ambiguousMeasurements(measuringCups1, low1, high1)
