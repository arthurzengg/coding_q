class Solution:
    """
    此解法用于判断字符串 s 是否为字符串 t 的子序列。
    思路：
    1. 使用两个指针 s_p 和 t_p 分别指向字符串 s 和 t 的起始位置。
    2. 遍历字符串 t，同时根据条件移动两个指针：
       - 如果 s[s_p] == t[t_p]，说明 s 的当前字符在 t 中找到匹配，同时移动两个指针。
       - 如果 s[s_p] != t[t_p]，只移动指针 t_p，继续在 t 中寻找匹配 s[s_p] 的字符。
    3. 如果 s 的所有字符都能在 t 中按序找到匹配，则返回 True。
    4. 如果遍历完 t 后，s 中还有字符未被匹配，则返回 False。

    方法：
    - isSubsequence(s, t): 输入字符串 s 和 t，判断 s 是否为 t 的子序列，并返回布尔值。
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_p = 0
        t_p = 0

        if s_len > t_len:
            return False

        while s_p < s_len and t_p < t_len:
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1
        return s_p == s_len
