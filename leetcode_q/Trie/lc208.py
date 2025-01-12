class Trie:
    """
    实现 Trie (前缀树) 数据结构。
    功能：
    - insert(word): 插入一个字符串到 Trie 中。
    - search(word): 检查 Trie 中是否完全包含某个字符串（非前缀形式）。
    - startsWith(prefix): 检查 Trie 中是否有字符串以该前缀开始。
    """

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        插入一个单词到 Trie 中。
        从 Trie 的根开始，逐步添加每个字符到 Trie 结构中，如果字符不存在，则创建新的字典节点。
        """
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

        cur['*'] = ''

    def search(self, word: str) -> bool:
        """
        搜索 Trie 中是否存在一个完整的单词。
        按照单词的每个字符逐层深入 Trie，如果在任何点字符路径中断，则该单词不存在。
        如果所有字符都正确匹配，最后检查是否有结束标记 '*'。
        """
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        if '*' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        检查 Trie 中是否有单词以指定的前缀开始。
        这类似于 search 方法，但不需要检查单词结束标记 '*'，只需要确认前缀路径存在。
        """
        cur = self.trie
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)