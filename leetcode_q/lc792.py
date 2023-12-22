from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        res = 0  # 用于存储匹配到的子序列数量
        lookup = defaultdict(list)  # 创建一个默认值为 list 的字典

        # 将 words 中的每个单词按其首字母分类并存储
        for word in words:
            lookup[word[0]].append(word)

        # 遍历字符串 s 中的每个字符
        for char in s:
            if char in lookup:
                # 获取以当前字符开头的所有单词列表
                check_list = lookup.pop(char)  # 弹出并返回该字符对应的单词列表
                for word in check_list:
                    # 如果单词长度为 1，表示找到了一个匹配的子序列
                    if len(word) == 1:
                        res += 1
                    else:
                        # 如果单词长度超过 1，将剩余部分加入到字典中相应的列表里
                        lookup[word[1]].append(word[1:])

        return res  # 返回匹配的子序列总数


sol = Solution()
print(sol.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
