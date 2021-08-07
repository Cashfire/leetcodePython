# Time:  O(n^2)
# Space: O(n)
#
# Given n points on a 2D plane, find_root the maximum number of points that lie on the same straight line.
#
import matplotlib.pyplot as plt

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        max_points = 0
        for i, start in enumerate(points):
            slope_count, same = {}, 1
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    slope = float("inf")
                    if start.x - end.x != 0:
                        slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    if slope not in slope_count:
                        slope_count[slope] = 1
                    else:
                        slope_count[slope] += 1

            current_max = same
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)

            max_points = max(max_points, current_max)

        return max_points


def lineThroughPoints(points):
    # y=mx+b, intercept b and slope m determine a unique line.
    if len(points) == 1:
        return 1
    max_pts = float('-inf')
    while points:
        x1, y1 = points.pop()
        slopes = {"vertical": 1}
        for x2, y2 in points:
            if x2 == x1:
                slopes["vertical"] += 1
                n = slopes["vertical"]
            else:
                slope = (y2 - y1) / (x2 - x1)
                n = slopes.get(slope, 1) + 1
                slopes[slope] = n

            if n > max_pts:
                max_pts = n
    return max_pts


def draw_points(points):
    plt.close()
    x, y = zip(*points)
    plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    # print(Solution().maxPoints([Point(), Point(), Point()]))
    points1 = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1]]
    points2 = [[1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[3, 1],[3, 2],[3, 4],[3, 5],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[5, 1],[5, 2],[5, 3],[5, 4],[5, 5],[6, 6],[2, 6]]
    # print(lineThroughPoints(points1))
    # draw_points(points2)
    print(lineThroughPoints(points2))
