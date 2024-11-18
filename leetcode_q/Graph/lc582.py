from collections import defaultdict, deque
from typing import List

class Solution:
    """
    # 思路：
    1. 创建一个从父进程ID到子进程ID列表的映射（字典），便于之后查找任何进程的所有直接子进程。
    2. 初始化一个队列，首先将要终止的进程ID `kill` 加入队列。
    3. 使用广度优先搜索（BFS）的方式处理队列中的进程：
       - 每次从队列中取出一个进程ID，将其加入结果列表。
       - 查找当前进程的所有子进程，并将这些子进程加入队列中，以便在接下来的迭代中处理。
    4. 继续执行步骤3，直到队列为空，此时结果列表中的所有进程ID即为需要终止的进程。
    5. 返回结果列表。
    """

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree_dict = defaultdict(list)
        n = len(pid)
        res = []

        # 构建每个进程的子进程列表
        for i in range(n):
            if ppid[i] == 0:
                continue
            tree_dict[ppid[i]].append(pid[i])

        # 初始化队列，开始广度优先搜索
        queue = deque()
        queue.append(kill)

        # BFS
        while queue:
            cur_kill = queue.popleft()
            res.append(cur_kill)
            if cur_kill in tree_dict:
                for child in tree_dict[cur_kill]:
                    queue.append(child)

        return res