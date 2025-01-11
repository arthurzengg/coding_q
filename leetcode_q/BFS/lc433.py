from collections import deque


class Solution:
    """
    中文思路解析：
    这道题的目标是找到从 startGene 变异到 endGene 的最少步数（每次只允许改变一个字符，且变异后必须在 bank 中）。

    我们可以使用 BFS（广度优先搜索）来求解，原因在于 BFS 天然可以求解“最短路径/最少步数”问题：
    1. 使用一个队列（queue）来存储当前的基因和已经使用的步数。
    2. 每次从队列中弹出一个基因（curGen），如果该基因等于 endGene，则返回当前步数（step）。
    3. 否则，就遍历该基因的每一位，将它替换成 'A', 'C', 'G', 'T' 中的每一个字符，生成一个新的基因（changedGen）。
    4. 如果新基因在 bank 中，说明这是一个合法的新状态，就把它加入队列中，步数加 1，并从 bank 中移除，避免重复。
    5. 如果所有可能的基因都遍历完还没找到 endGene，就返回 -1。

    关键点：
    - BFS 能保证第一次到达 endGene 时，所用的步数就是最小步数。
    - 每次发现一个新的基因后，需要立即从 bank 中删除该基因，防止重复入队，减少不必要的搜索。
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if endGene not in bank:
            return -1

        queue = deque()
        queue.append((startGene, 0))

        while queue:
            curGen, step = queue.popleft()
            if curGen == endGene:
                return step

            for i in range(len(curGen)):
                for c in 'ACGT':
                    changedGen = curGen[:i] + c + curGen[i + 1:]
                    if changedGen in bank and changedGen != curGen:
                        queue.append((changedGen, step + 1))
                        bank.remove(changedGen)

        return -1