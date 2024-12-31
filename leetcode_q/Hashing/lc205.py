class Solution:
    """
    要判断两个字符串 s 和 t 是否同构（isomorphic），核心思想就是：
    1. 如果 s 中的某个字符在位置 i 第一次出现，那么 t 中对应的字符在位置 i 也必须是第一次出现；
    2. 如果是第二次出现，那么对应的字符也必须是第二次出现；依此类推。换句话说，s 中每个字符出现的次序必须和 t 中对应字符出现的次序一一对应。

    思路：
    1. 使用两个字典 s_index 和 t_index 来分别记录字符串 s 和 t 中每个字符第一次出现的位置。
    2. 遍历字符串 s 和 t 的每个字符：
       - 如果当前字符是第一次出现，则记录其在字符串中的索引。
       - 检查当前遍历到的字符在两个字符串中第一次出现的位置是否相同：
         如果不同，立即返回 False，因为这表明不能通过简单的字符替换来同构两个字符串。
    3. 如果所有字符的第一次出现位置都相同，则两个字符串是同构的，返回 True。
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index = {}
        t_index = {}
        for i in range(len(s)):
            if s[i] not in s_index:
                s_index[s[i]] = i
            if t[i] not in t_index:
                t_index[t[i]] = i
            if s_index[s[i]] != t_index[t[i]]:
                return False
        return True