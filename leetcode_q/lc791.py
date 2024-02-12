class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        s = list(s)
        for char in order:
            while char in s:
                res += char
                s.remove(char)
        if not s:
            return res
        else:
            for char in s:
                res += char
            return res

sol = Solution()
print(sol.customSortString("kqep", "pekeq"))
# Output: kqeep

# 这个是优化后的代码
# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         # 统计 s 中每个字符出现的次数
#         count_s = Counter(s)
#         res = ''
#
#         # 按照 order 的顺序添加字符到结果字符串
#         for char in order:
#             if char in count_s:
#                 res += char * count_s[char]
#                 del count_s[char]  # 移除已经处理过的字符
#
#         # 添加剩余的字符
#         for char, count in count_s.items():
#             res += char * count
#
#         return res
