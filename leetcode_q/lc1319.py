from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 如果线缆的数量少于 n-1，则不可能将所有计算机连接起来
        if len(connections) < n - 1:
            return -1

        # 使用 defaultdict 创建邻接列表，存储网络连接信息
        edges = defaultdict(list)

        # 构建无向图
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)

        # 使用集合 seen 记录已经访问过的节点
        seen = set()

        # 深度优先搜索（DFS）函数，用于探索每一个组件
        def dfs(u):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)

        # 计算需要连接的组件数量
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)

        # 返回需要的最少线缆数，即连接所有组件所需的额外线缆数
        return ans - 1


n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

sol = Solution()
print(sol.makeConnected(n, connections)) # Output = 2
