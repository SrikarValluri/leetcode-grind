from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = defaultdict(list)
        for point in points:
            dist = point[0]**2 + point[1]**2
            distance[dist].append(point)

        closest = sorted(distance.items(), key=lambda x: x[0])
        kclosest = []
        for i in range(len(closest)):
            for j in range(len(closest[i][1])):
                kclosest.append(closest[i][1][j])
                k -= 1
                if k == 0:
                    return kclosest
