class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        opening = "({["
        closing = ")}]"
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if len(stack) == 0 or opening.index(stack.pop()) != closing.index(char):
                    return False
        return len(stack) == 0
                