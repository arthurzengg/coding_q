from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        # 添加一条从 start 到 end 的边到图中
        self.graph[start].append(end)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = Graph()
        # 根据先修课程列表构建图
        for pre in prerequisites:
            g.addEdge(pre[1], pre[0])

        # 初始化 in_degree 字典，存储每个课程的入度（依赖它的课程数）
        in_degree = {i: 0 for i in range(numCourses)}

        # 更新 in_degree 根据先修课程
        print(g.graph)
        for node in g.graph.keys():
            for adj in g.graph[node]:
                in_degree[adj] += 1

        # 使用队列来进行拓扑排序，首先加入所有入度为0的课程
        print(in_degree)
        queue = []
        for node, degree in in_degree.items():
            if degree == 0:
                queue.append(node)

        # 存储拓扑排序的结果
        sorted_order = []
        while queue:
            # 从队列中取出一个课程
            u = queue.pop(0)
            sorted_order.append(u)

            # 减少与 u 相关的所有课程的入度
            # 如果某课程入度降至0，加入队列
            for v in g.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # 检查是否所有课程都被排序（即没有环）
        # 如果 sorted_order 的长度与图中节点数相等，说明没有环
        if len(sorted_order) == numCourses:
            return sorted_order
        else:
            return []


sol = Solution()
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# Output: [0, 1, 2, 3]