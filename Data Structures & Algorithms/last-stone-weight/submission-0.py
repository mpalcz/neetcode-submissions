class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)
            new_weight = largest - second_largest
            if new_weight:
                heapq.heappush(stones, -new_weight)
        if not stones:
            return 0
        return -heapq.heappop(stones)