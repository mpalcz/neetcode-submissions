class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        letters = {all_letters[i]: 0 for i in range(26)}

        for char in s:
            letters[char] += 1
        
        for char in t:
            if letters[char] == 0:
                return False
            else:
                letters[char] -=1
        
        return True
