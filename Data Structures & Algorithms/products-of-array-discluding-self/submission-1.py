class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumulative = []
        num_zeros = 0
        left = right = 1
        # traverse to the right
        for num in nums:
            if not num:
                num_zeros += 1
                if num_zeros == 2:
                    return [0]*len(nums)
            cumulative.append([right])
            right *= num

        # traverse to the left
        for i in range(len(nums)-1, -1, -1):
            cumulative[i].append(left)
            left *= nums[i]
            
        ret = []
        # combine information
        for left_val, right_val in cumulative:
            ret.append(left_val*right_val)
        return ret
