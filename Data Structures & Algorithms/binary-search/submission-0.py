class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target: 
            return -1
        return self.binarySearch(nums, 0, len(nums)-1, target)

    def binarySearch(self, nums: List[int], l: int, r: int, target: int):
        if r < l:
            return -1
        middle = l + (r-l)//2
        if target < nums[middle]:
            return self.binarySearch(nums, l, middle-1, target)
        elif target > nums[middle]:
            return self.binarySearch(nums, middle+1, r, target)
        else:
            return middle
        