class Solution:
    def wordsTyping(self, sentence, rows, cols):
        n = len(sentence)
        memo = [0] * n

        # 已不同的单词作为开头，每个可以在一行中最多放多少个
        for i in range(n):
            index = i
            words = 0
            cols_len = 0
            # index % n的作用就是不断对sentence进行循环 ex 4 % 3 = 1
            while cols_len + len(sentence[index]) <= cols:
                words += 1
                cols_len += len(sentence[index]) + 1
                index = (index + 1) % len(sentence)
            memo[i] = words

        # 一共可以放几个单词
        words = 0
        index = 0
        for i in range(rows):
            # 遍历每一行，使用 memo[index] 得到从当前单词开始
            words += memo[index]
            # 更新 index 以指向下一行的起始单词
            index = (memo[index] + index) % n

        return words // n

# 示例使用
sol = Solution()
print(sol.wordsTyping(["a", "bcd", "e"], 3, 6))  # 示例输入

# Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
# Output: 2
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
# The character '-' signifies an empty space on the screen.

# memo = [2, 2, 2]
# words = 6
# words // n = 6 // 3 = 2
