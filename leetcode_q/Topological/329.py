class Solution:
    """
    中文思路解析（拓扑排序法）：
    题目要求找出矩阵中最长的严格递增路径。可以将矩阵看成一张有向无环图（DAG），
    - 每个点为一个节点；
    - 如果一个点的邻居值比它大，则它可以“跳”过去，构成一条有向边。

    解法核心：拓扑排序 + 层序遍历（多源 BFS）
    1. 统计每个点的“出度”，即能跳向的更大邻居个数。
    2. 所有“出度为 0” 的点，即不能跳向任何更大值的点，作为起始点入队。
    3. 使用 BFS 一层层向前推进，每遍历一层，路径长度 +1。
    4. 在每一层中，将指向当前节点的“入边”的节点出度减 1，若减为 0，则说明它也可以进入下一层。

    最终遍历的层数即为矩阵中最长递增路径的长度。

    时间复杂度：O(m * n)
    空间复杂度：O(m * n)
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        out_degree = [[0 for _ in range(n)] for _ in range(m)]

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i in range(m):
            for j in range(n):
                count = 0
                for dx, dy in directions:
                    nexti = i + dx
                    nextj = j + dy
                    if 0 <= nexti < m and 0 <= nextj < n and matrix[nexti][nextj] > matrix[i][j]:
                        count += 1
                out_degree[i][j] = count

        queue = []
        for i in range(m):
            for j in range(n):
                if out_degree[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for dx, dy in directions:
                    nexti = i + dx
                    nextj = j + dy
                    if 0 <= nexti < m and 0 <= nextj < n and matrix[i][j] > matrix[nexti][nextj]:
                        out_degree[nexti][nextj] -= 1
                        if out_degree[nexti][nextj] == 0:
                            queue.append((nexti, nextj))
            print(queue)
        return ans