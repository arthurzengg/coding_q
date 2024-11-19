from collections import defaultdict
from typing import List


class Solution:
    """
    # 思路：
    1. 使用深度优先搜索（DFS）遍历从起点出发的所有路径。
    2. 引入节点状态来标记访问情况：
       - 0：未访问
       - 1：正在访问（当前路径上）
       - 2：已访问（所有从该节点出发的路径均已验证）
    3. 在DFS过程中：
       - 如果遇到状态为1的节点，说明存在环，返回False。
       - 如果当前节点是叶子节点（无出边），检查是否为终点，不是则返回False。
    4. 对于每个节点，只有当其所有后继节点都返回True时，才能标记为已访问状态2。
    5. 如果DFS从起点出发返回True，说明所有路径均能到达终点，且无环存在。
    """

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        state = [0] * n  # 节点状态：0=未访问，1=正在访问，2=已访问

        def dfs(node):
            if state[node] != 0:
                # 如果状态为1，说明存在环；状态为2，说明已验证过
                return state[node] == 2
            if not graph[node]:
                # 如果是叶子节点，必须检查是否为终点
                return node == destination
            state[node] = 1  # 标记为正在访问
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2  # 标记为已访问
            return True

        # 如果终点有出边，说明可能有离开终点的路径，返回False
        if graph[destination]:
            return False

        return dfs(source)