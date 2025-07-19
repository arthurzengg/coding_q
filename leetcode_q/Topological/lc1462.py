class Solution:
    """
    整体思路为：构建反向图 + 每个查询执行一次 BFS。

    1. 构图：
    - 建立邻接表（反向图），将每条边 (u, v) 反向为 v → u；
    - 这样在查询过程中可以从 v 出发向前寻找它的所有前置课程。

    2. 对每个查询 (u, v)：
    - 从 v 开始进行 BFS 向前遍历；
    - 若在遍历过程中遇到 u，说明 u 是 v 的某个先修课，返回 True；
    - 若队列耗尽仍未找到，则说明不是先修课，返回 False。

    3. 使用 visited 集合避免重复访问节点，提升效率，防止陷入环或重复搜索。

    时间复杂度：O(Q × E)，Q 为查询数量，E 为图中的边数。
    空间复杂度：O(N + E)
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        n = len(prerequisites)
        res = []
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for i in range(n):
            u = prerequisites[i][0]
            v = prerequisites[i][1]
            graph[v].append(u)

        for u, v in queries:
            found = False
            visited = set()
            queue = [v]
            while queue:
                node = queue.pop(0)
                visited.add(node)
                for pre in graph[node]:
                    if pre == u:
                        found = True
                        break
                    if pre not in visited:
                        queue.append(pre)
                if found:
                    break
            res.append(found)
        return res

