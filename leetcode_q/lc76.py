from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 如果s的长度小于t的长度，则无法形成窗口，直接返回空字符串
        if len(s) < len(t):
            return ''

        # 使用Counter统计t中的字符及其出现次数
        char_dict = Counter(t)
        # 初始化左右指针和字符串s的长度
        l = r = 0
        n = len(s)
        # 初始化最小长度为无穷大，用于记录最小窗口的长度
        min_len = float('inf')
        # 需要匹配的字符数量，初始为t的长度
        needCnt = len(t)
        # 记录最小窗口的起始索引
        startIndex = 0

        # 遍历字符串s
        while r < n:
            # 如果当前字符在t中，减少需要匹配的字符数量
            if char_dict[s[r]] > 0:
                needCnt -= 1
            # 无论如何都减少char_dict中对应字符的计数
            char_dict[s[r]] -= 1

            # 如果已经匹配了所有t中的字符
            if needCnt == 0:
                # 尝试缩小窗口，移动左指针，直到不能再缩小为止
                while True:
                    if char_dict[s[l]] == 0:
                        break
                    char_dict[s[l]] += 1
                    l += 1
                # 记录当前窗口长度，并更新最小窗口长度
                temp = min_len
                min_len = min(min_len, r - l + 1)
                # 如果找到了更小的窗口，则更新起始索引
                if temp != min_len:
                    startIndex = l
                # 移动左指针，准备寻找新的窗口
                char_dict[s[l]] += 1
                l += 1
                needCnt += 1

            # 移动右指针，继续寻找新的窗口
            r += 1

        # 如果min_len仍为无穷大，说明没有找到符合条件的窗口，返回空字符串
        if min_len == float('inf'):
            return ''
        # 返回找到的最小窗口子串
        return s[startIndex:startIndex + min_len]



sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
# Output: BANC