class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2
        
        contains = {}
        window_contains = {}
        for char in s1:
            contains[char] = contains.get(char, 0) + 1
        
        l = r = 0
        window_len = len(s1)
        while r < len(s2):
            window_contains[s2[r]] = window_contains.get(s2[r], 0) + 1
            if (r - l + 1) == window_len: 
                if contains != window_contains:
                    window_contains[s2[l]] -= 1
                    if window_contains[s2[l]] == 0:
                        del window_contains[s2[l]]
                    l += 1
                else:
                    return True
            r += 1
        return False

