class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        anagram_groups = defaultdict(list)
        for word in strs:
            local_hash = [0]*26
            for letter in word:
                local_hash[ord(letter) - ord('a')] += 1
            anagram_groups[tuple(local_hash)].append(word)

        return list(anagram_groups.values())