class Solution:
    """
    与lc205同理
    思路：
    1. 使用两个字典 s_index 和 p_index 来记录字符串 s 中的单词和模式 pattern 中的字符第一次出现的位置。
    2. 先将字符串 s 按空格切分成单词列表。
    3. 如果单词列表的长度与模式字符串的长度不相同，则直接返回 False，因为它们无法对应匹配。
    4. 遍历模式字符串 pattern 的每一个字符：
       - 如果当前字符或单词是第一次出现，则在对应的字典中记录它的索引。
       - 检查当前字符和单词在两个字典中记录的第一次出现位置是否相同：
         如果不同，则返回 False，因为这表明模式与单词之间的映射关系不一致。
    5. 遍历结束后，如果所有字符和单词的映射关系都保持一致，则返回 True，表示字符串 s 符合给定的模式 pattern。
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        s_index = {}
        p_index = {}

        s = s.split(' ')
        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] not in p_index:
                p_index[pattern[i]] = i
            if s[i] not in s_index:
                s_index[s[i]] = i
            if p_index[pattern[i]] != s_index[s[i]]:
                return False
        return True
