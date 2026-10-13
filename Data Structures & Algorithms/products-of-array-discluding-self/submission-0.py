class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ret = []
        num_zeroes = 0
        single_zero_ind = -1
        for ind, num in enumerate(nums):
            if num == 0:
                num_zeroes += 1
                single_zero_ind = ind
                if num_zeroes == 2:
                    return [0]*len(nums)
            else:
                mul *= num
        if num_zeroes:
            ret = [0]*len(nums)
            ret[single_zero_ind] = mul
        else: 
            for num in nums:
                if num == 0:
                    ret.append(mul)
                else:
                    ret.append(int(mul/num))
        return ret
