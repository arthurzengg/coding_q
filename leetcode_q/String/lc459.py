class Solution:
    """
    解法步骤：
    1. 枚举子串的长度 i，从 1 到 n - 1（n 是字符串长度）。
    2. 如果当前长度 i 能整除字符串长度 n（即 n % i == 0），说明可以尝试用这个子串去构造原字符串。
    3. 判断 s[0:i] 这个子串重复 (n // i) 次后是否等于原字符串。
    4. 一旦找到符合条件的子串，就返回 True。
    5. 如果没有任何子串符合，返回 False。

    时间复杂度：O(n^2)，因为最多检查 n-1 个子串，每个子串拼接验证耗时 O(n)
    空间复杂度：O(n)，主要用于字符串复制生成。
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n):
            if n % len(s[0:i]) == 0:
                if s[0:i] * (n // len(s[0:i])) == s:
                    return True
        return False
