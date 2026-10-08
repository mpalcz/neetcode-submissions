class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set()
        for num in nums:
            visited.add(num)
        lefts = []
        for num in nums:
            if num - 1 not in visited and num + 1 in visited:
                lefts.append(num)
        if not lefts:
            return 1
        max_count = 0
        for left in lefts:
            value = left
            count = 0
            while value in visited:
                count += 1
                value += 1
            max_count = max(max_count, count)
        return max_count
        