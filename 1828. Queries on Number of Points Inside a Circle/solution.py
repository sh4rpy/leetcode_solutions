class Solution:
    def countPoints(
        self, points: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        ans = []
        for query in queries:
            count_points_inside = 0
            for point in points:
                if (query[0] - point[0]) ** 2 + (query[1] - point[1]) ** 2 <= query[
                    2
                ] ** 2:
                    count_points_inside += 1
            ans.append(count_points_inside)
        return ans
