from typing import List


class Solution:
    """
    # 思路：
    1. 创建一个布尔数组 `boolean`，其长度与字符串 `s` 相同。这个数组用于标记需要加粗的字符位置。
    2. 遍历字符串 `s`，对每个位置尝试匹配列表 `words` 中的每个单词。
       - 如果在位置 `i` 发现 `words` 中的某个单词，将 `boolean` 数组从 `i` 到 `i + len(word) - 1` 的位置标记为 `True`。
    3. 根据 `boolean` 数组的标记，构建最终的结果字符串。
       - 遍历 `boolean` 数组，每遇到一个 `True` 的起始位置（前一个位置不是 `True`），在结果中添加 `<b>`。
       - 添加当前字符。
       - 每遇到一个 `True` 的结束位置（下一个位置不是 `True` 或当前位置是字符串的最后位置），在结果中添加 `</b>`。
    4. 返回构建好的字符串，其中包含了必要的加粗标签。
    """

    def addBoldTag(self, s: str, words: List[str]) -> str:
        boolean = [False for _ in range(len(s))]  # 步骤1

        i = 0
        while i < len(s):  # 步骤2
            for word in words:
                if s[i:i + len(word)] == word:  # 如果在位置 i 匹配到 word
                    for j in range(len(word)):
                        boolean[j + i] = True  # 标记需要加粗的位置
            i += 1

        res = []  # 步骤3
        for i in range(len(boolean)):
            if boolean[i] and (i == 0 or not boolean[i - 1]):  # 加粗开始标签
                res.append('<b>')
            res.append(s[i])  # 添加字符
            if boolean[i] and (i == len(s) - 1 or not boolean[i + 1]):  # 加粗结束标签
                res.append('</b>')

        return ''.join(res)  # 步骤4，返回结果字符串