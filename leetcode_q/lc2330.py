class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 4:
            return True
        half = n // 2
        s_reverse = s[::-1]
        difference = 0
        for i in range(half):
            if s[i] != s_reverse[i]:
                difference += 1
        if difference <= 2:
            return True
        else:
            return False
