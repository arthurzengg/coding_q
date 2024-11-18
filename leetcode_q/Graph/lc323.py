class Solution:
    """
    # 思路：
    1. 构建图：使用邻接表形式，对于每个输入的边，将两个节点相互关联。
    2. 深度优先搜索（DFS）：定义一个递归函数来遍历所有与当前节点相连的节点，标记为已访问。
    3. 连通分量的计数：对于每一个未访问过的节点，执行一次DFS，每发现一个新的连通分量，结果计数加1。
    4. 细节处理：使用集合来跟踪已访问过的节点，确保每个节点只被访问一次。
    """

    def countComponents(self, num_nodes: int, edges: List[List[int]]) -> int:
        def dfs(node):
            # 如果节点已访问，直接返回0，不计入新的连通分量
            if node in visited:
                return 0
            visited.add(node)
            # 访问所有与当前节点直接相连的节点
            for neighbor in graph[node]:
                dfs(neighbor)
            # 完成对一个连通分量的访问，返回1
            return 1

        result = 0
        graph = defaultdict(list)
        # 构建图的邻接表
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        # 遍历所有节点，对未访问的节点执行DFS
        for current_node in range(num_nodes):
            result += dfs(current_node)  # 只有当启动了新的DFS时，才会加1

        return result