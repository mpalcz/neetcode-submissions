class Solution:

    def encode(self, strs: List[str]) -> str:
        string_return = ""
        for word in strs:
            size_string = str(len(word))
            val = "[" + "0"*(3-len(size_string)) + size_string + "]"
            temp = val + word + "0"*(200-len(word))
            string_return += temp
        return string_return

    def decode(self, s: str) -> List[str]:
        result = []
        for k in range(int(len(s)/205)):
            temp = s[k*205:(k+1)*205]
            size = int(temp[1:4])
            result.append(temp[5:5+size])
        return result

