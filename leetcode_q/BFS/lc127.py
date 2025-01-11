class Solution:
    """
    和lc433思路一样，但用了visited，而不是remove，会更快
    中文思路解析：
    我们要从 beginWord 一步步变换为 endWord，每次只能改动单词中的一个字符，且改动后的单词必须在 wordList 中。

    使用 BFS（广度优先搜索）可以高效地找到最短路径：
    1. 把 beginWord 入队，并将步数初始化为 1（表示第一层/第一个单词）。
    2. 从队列中依次弹出当前单词 curWord，并检查其是否等于 endWord；若是，则返回当前步数 step。
    3. 如果不是，就遍历 curWord 的每一位字符，尝试替换为 'a' - 'z' 中的每个字母
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        visited = set([beginWord])

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            curWord, step = queue.popleft()
            if curWord == endWord:
                return step

            for i in range(len(curWord)):
                for c in 'abcdefghyijklmnopqrstuvwxyz':
                    changedWord = curWord[:i] + c + curWord[i + 1:]
                    if changedWord in wordList and changedWord not in visited:
                        queue.append((changedWord, step + 1))
                        visited.add(changedWord)

        return 0