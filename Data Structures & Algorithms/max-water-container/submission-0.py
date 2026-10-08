class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            capacity = width*height
            res = max(res, capacity)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return res
