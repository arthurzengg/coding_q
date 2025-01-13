from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.word = ''

    def insert(self, word):
        # 在这里self指的就是root
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    """
    中文思路解析：
    这是一个支持添加和搜索操作的数据结构，特别支持使用 '.' 作为通配符进行模糊搜索。
    具体实现方法如下：

    1. 使用 TrieNode 类构建前缀树（Trie），每个节点都可能指向若干个子节点，并可能标记为某个单词的结束。
    2. 添加单词时，从根节点开始，依次将单词的每个字母作为键在当前节点的子节点中查找，如果不存在则创建新的 TrieNode。
    3. 完成单词添加后，在单词的最后一个字母对应的节点上标记结束，并存储单词。
    4. 搜索单词时，使用广度优先搜索（BFS）。对于每个字符：
       - 如果是普通字符，直接在当前层的节点中查找对应的子节点。
       - 如果是通配符 '.'，则需要将当前层的所有子节点加入到下一层的搜索中。
    5. 搜索结束后，检查是否存在标记为单词结尾的节点，存在则表示找到匹配的单词。

    关键点：
    - 使用 Trie 结构可以高效地添加和搜索单词。
    - 使用 BFS 处理通配符搜索，允许同时在多个分支上进行探索。
    - 通过在 TrieNode 中直接存储单词来快速完成匹配检查。
    """

    def __init__(self):
        self.ans = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                self.dfs(i, j, root, board, n, m)

        return list(self.ans)

    def dfs(self, i, j, node, board, n, m):
        if board[i][j] not in node.children:
            return

        c = board[i][j]
        next_node = node.children[c]

        if next_node.word != '':
            self.ans.add(next_node.word)
            next_node.word = ''

        board[i][j] = '#'

        for next_i, next_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= next_i < n and 0 <= next_j < m:
                self.dfs(next_i, next_j, next_node, board, n, m)
        board[i][j] = c