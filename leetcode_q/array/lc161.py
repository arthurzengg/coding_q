class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        min_len = min(len(s), len(t))
        for i in range(min_len):
            if s[i] != t[i]:
                if len(s) == len(t):  # 如果长度相同，检查替换当前字符后，剩余部分是否相同
                    return s[i + 1:] == t[i + 1:]
                elif len(s) < len(t):  # 如果 s 较短，检查 s 从当前位置开始的剩余部分是否与 t 从下一位置开始的剩余部分相同
                    return s[i:] == t[i + 1:]
                else:  # 如果 s 较长，检查 s 从下一位置开始的剩余部分是否与 t 从当前位置开始的剩余部分相同
                    return s[i + 1:] == t[i:]
        # 循环结束，若没有不匹配的字符，则最后检查两字符串的长度差是否为1
        return abs(len(s) - len(t)) == 1


