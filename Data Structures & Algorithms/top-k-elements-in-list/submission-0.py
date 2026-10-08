class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        hashh = [[] for i in range(len(nums) + 1)]
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        result = []
        for val, cnt in frequencies.items():
            hashh[cnt].append(val)

        res = []
        for i in range(len(hashh) - 1, 0, -1):
            if not hashh[i]:
                continue
            for num in hashh[i]:
                res.append(num)
                if len(res) == k:
                    return res