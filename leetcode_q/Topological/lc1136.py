from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # 思路解析：
        # 我们需要找到完成所有课程所需的最少学期数，其中一些课程可能有先修课程。
        # 这是一个典型的拓扑排序问题，可以使用广度优先搜索（BFS）来解决。
        # 具体步骤如下：
        # 1. 计算每个课程的入度（即需要先修的课程数量）。
        # 2. 建立课程之间的依赖关系图（邻接表）。
        # 3. 将所有入度为0的课程（没有先修课程）加入队列，表示可以立即开始学习的课程。
        # 4. 使用BFS遍历，每一层代表一个学期。在每个学期，我们可以同时学习所有当前入度为0的课程。
        # 5. 对于每个学过的课程，更新其后续课程的入度。如果后续课程的入度减为0，表示其先修课程已全部完成，可以在下一个学期学习，将其加入队列。
        # 6. 统计已学习的课程数量，如果等于总课程数，返回学期数；否则，说明存在环，无法完成所有课程，返回-1。

        in_degree = {i: 0 for i in range(1, n + 1)}  # 入度是图论算法中重要的概念之一。它通常指有向图中某点作为图中边的终点的次数之和。
        graph = defaultdict(list)
        for u, v in relations:
            graph[u].append(v)
            in_degree[v] += 1

        # 初始化队列，添加所有入度为零的节点
        queue = deque([node for node in in_degree if in_degree[node] == 0])

        semesters = 0  # 学期计数
        studied_courses = 0  # 已学习的课程数量

        while queue:
            semesters += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                studied_courses += 1
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        # 检查是否学习了所有课程
        if studied_courses == n:
            return semesters
        else:
            return -1