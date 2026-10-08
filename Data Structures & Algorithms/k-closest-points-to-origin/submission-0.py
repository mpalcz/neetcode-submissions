class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        if k == 0:
            return []
        
        distances = []
        for point in points:
            x, y = point
            dist = x**2 + y**2
            distances.append((-dist, point))
        res = distances[:k]
        heapq.heapify(res)
        for dist, point in distances[k:len(distances)]:
            heapq.heappush(res, (dist, point))
            heapq.heappop(res)
        return [point for dist, point in res]

