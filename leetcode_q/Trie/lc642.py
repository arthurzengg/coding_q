from collections import defaultdict
class TrieNode:
    """ Trie节点定义，每个节点存储其字符、热门列表和子节点的引用。 """

    def __init__(self, name):
        self.name = name
        self.hot_list = []
        self.next = defaultdict(TrieNode)


class AutocompleteSystem:
    """
    # 思路：
    1. 使用前缀树（Trie）来存储所有句子及其频率。
    2. 每个节点都有一个热门列表，该列表按频率降序（如果频率相同，则按字典序）排序存储句子。
    3. 用户输入字符时，沿前缀树下行并更新当前的热门列表，如果输入'#'，则将当前输入句子存入前缀树并重置输入状态。
    """

    def __init__(self, sentences: List[str], times: List[int]):
        self.head = TrieNode('')
        self.input_list = []
        n = len(sentences)
        for i in range(n):
            self.insert(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        cur = self.head
        if c == '#':
            self.insert(''.join(self.input_list), 1)
            self.input_list = []
            return []
        self.input_list.append(c)
        res = []
        for c in self.input_list:
            if c in cur.next:
                cur = cur.next[c]
            else:
                return []
        if len(cur.hot_list) <= 3:
            return [sentence for hot, sentence in cur.hot_list]
        else:
            for i in range(3):
                res.append(cur.hot_list[i][1])
        return res

    def insert(self, word, hot):
        cur = self.head
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode(c)
            if any(word in sublist for sublist in cur.next[c].hot_list):
                for sublist in cur.next[c].hot_list:
                    if word in sublist:
                        sublist[0] += 1
            else:
                cur.next[c].hot_list.append([hot, word])
            cur.next[c].hot_list = sorted(cur.next[c].hot_list, key=lambda x: (-x[0], x[1]))
            cur = cur.next[c]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)