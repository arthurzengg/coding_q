class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        题目要求将所有点连通，边的权重为曼哈顿距离，目标是找到连接所有点的最小代价。
        这实际上是一个典型的最小生成树（Minimum Spanning Tree，MST）问题。

        解法采用 Prim 算法：
        1. 初始化每个点到最小生成树的最小距离 `minDist[i]`，初始为 ∞，第 0 个点设为 0（从它出发）。
        2. 用一个 `visited` 集合记录已经加入 MST 的点。
        3. 每次从未访问的点中，选出当前 `minDist` 最小的点 `minNode` 加入 MST，并将对应边权加入结果 `res`。
        4. 加入新节点后，尝试用它来更新其他未访问节点的最小连边距离（曼哈顿距离）。
        - 曼哈顿距离计算公式为：`|x1 - x2| + |y1 - y2|`

        重复上述过程直到所有点都加入 MST，最终 `res` 就是最小连接成本。

        时间复杂度：O(n²)，因为每轮都需要遍历所有节点来选最近的点，并更新其他节点的距离。对于 n <= 1000 的数据规模是可接受的。
        """
        n = len(points)
        minDist = [float('inf') for _ in range(n)]
        res = 0
        visited = set()
        minDist[0] = 0  # 从 0 号点出发
        while len(visited) < n:
            # 选择未访问节点中，与已建成 MST 距离最小的那个
            minVal = float('inf')
            for i, dist in enumerate(minDist):
                if i not in visited and minDist[i] < minVal:
                    minNode = i
                    minVal = minDist[i]

            # 把这条边权加进答案，并把节点放进已访问集合
            res += minVal
            visited.add(minNode)

            # 用新加入的节点去松弛其余未访问节点的最小距离
            for j in range(n):
                if j in visited:
                    continue
                manDist = abs(points[j][0] - points[minNode][0]) + abs(points[j][1] - points[minNode][1])
                minDist[j] = min(minDist[j], manDist)

        return res

