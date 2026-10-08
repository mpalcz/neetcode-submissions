class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        num_sorted = sorted(nums)
        l = 0
        r = len(nums) - 1
        while True:
            sum = num_sorted[l] + num_sorted[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                break
        result = []
        for i in range(len(nums)):
            if nums[i] == num_sorted[l] or nums[i] == num_sorted[r]:
                result.append(i)
                if len(result) == 2:
                    break
        return result

