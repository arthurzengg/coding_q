from collections import deque


class WordDictionary:
    """
    实现一个支持添加新单词和搜索字符串的数据结构，其中搜索支持点 '.' 作为通配符，可以匹配任何单个字母。

    功能：
    - addWord(word): 向字典中添加一个新的单词。
    - search(word): 在字典中搜索可能含有通配符 '.' 的字符串。

    使用的数据结构：
    - 使用 trie (前缀树) 来存储单词，使得添加和搜索操作都能高效进行。
    - 使用广度优先搜索（BFS）来处理包含 '.' 通配符的搜索，以便同时在多个分支上进行搜索。

    广度优先搜索（BFS）特别适合这里的用途，因为它可以同时在多个可能的分支上进行扩展，特别是当遇到通配符时。
    """

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        queue = deque()
        queue.append(self.root)
        for c in word:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if c == '.':
                    for new_c in 'abcdefghijklmnopqrstuvwxyz':
                        if new_c in cur:
                            queue.append(cur[new_c])
                if c in cur:
                    cur = cur[c]
                    queue.append(cur)
        for res in queue:
            if '*' in res:
                return True
        return False

