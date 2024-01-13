from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0  # 初始化答案为0

        # 遍历所有可能的不同字符数量（最多26个字母）
        for i in range(1, 27):
            left, right = 0, 0  # 初始化滑动窗口的左右边界
            window_count = 0  # 窗口中不同字符的数量
            letter_map = defaultdict(int)  # 字符计数映射
            less_k_count = 0  # 记录窗口中字符计数小于k的数量

            while right < n:
                # 增加右边界字符的计数
                letter_map[s[right]] += 1

                # 当前字符首次出现，更新窗口中不同字符数量和小于k计数
                if letter_map[s[right]] == 1:
                    window_count += 1
                    less_k_count += 1
                # 当前字符达到k次，减少小于k计数
                if letter_map[s[right]] == k:
                    less_k_count -= 1

                # 当窗口中不同字符数量超过i，缩小左边界
                while window_count > i:
                    letter_map[s[left]] -= 1
                    # 当前字符计数降为0，更新不同字符数量和小于k计数
                    if letter_map[s[left]] == 0:
                        window_count -= 1
                        less_k_count -= 1
                    # 当前字符计数由k变为k-1，增加小于k计数
                    elif letter_map[s[left]] == k - 1:
                        less_k_count += 1
                    left += 1

                # 如果窗口中所有字符的计数都大于等于k，更新答案
                if less_k_count == 0:
                    # 答案为当前窗口的长度
                    ans = max(ans, right - left + 1)
                right += 1
        return ans


# 示例
sol = Solution()
print(sol.longestSubstring("aaabb", 3))  # 示例输入
# Output: 3