# 解析：
# 1. 字符串中会有数字也需要被考虑，所以要用char.isalnum()
#
# Note:
# isalpha() 返回 True 当且仅当字符是字母。
# isdigit() 或 isnumeric() 返回 True 当且仅当字符是数字。
# isalnum() 返回 True 当且仅当字符是字母或数字。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted_chars = ''
        for char in s:
            if char.isalpha() or char.isalnum():
                extracted_chars += char
        extracted_chars = extracted_chars.lower()
        if extracted_chars == extracted_chars[::-1]:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome('0P0'))
# Output: True