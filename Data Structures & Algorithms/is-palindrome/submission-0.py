class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s or len(s) == 1:
            return True
        forward = 0
        backward = len(s) - 1
        while forward < backward:
            while not s[forward].isalnum():
                forward += 1
                if forward == backward or forward == len(s):
                    return True
            while not s[backward].isalnum():
                backward -= 1
                if backward == forward or backward == -1:
                    return True
            if s[forward].lower() != s[backward].lower():
                return False
            forward += 1
            backward -= 1
            
        return True