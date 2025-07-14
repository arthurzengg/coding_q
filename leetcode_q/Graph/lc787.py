class Solution:
    """
    思路解析：
    1. 将所有航班信息构造成邻接表 graph，其中 graph[u] 存储从 u 出发的 (v, w) 列表，表示飞到 v 的票价为 w。
    2. 定义 best[i][j] 表示恰好使用了 j 段航班（即 j−1 次中转）到达节点 i 的最小花费。由于允许最多 k 次中转，故最多使用 k+1 段航班，
       j 的取值范围是 0 到 k+1，共 k+2 个状态。
    3. 初始化时，best[src][0] = 0，其余状态均设为 +∞，表示尚不可达。
    4. 使用一个最小堆（priority queue）维护待扩展状态，堆中元素为 (当前累计花费 cost, 当前节点 u, 已用航段数 stops)。
    5. 每次从堆里取出 cost 最小的状态：
       - 若 u == dst，则直接返回 cost（此时必是最优解）。
       - 若 stops 已经超过 k，则无法继续中转，跳过。
    6. 否则遍历 graph[u] 的所有出边 (v, w)，计算 new_cost = cost + w，
       若 new_cost < best[v][stops+1]，则更新 best[v][stops+1] 并将 (new_cost, v, stops+1) 推入堆中。
    7. 若堆耗尽仍未到达 dst，则返回 -1，表示无法在 k 次中转内到达目的地。

    时间复杂度：O((k+1)·E·log((k+1)·E))，其中 E 为航班数量，k+1 是最多允许的航段数。
    空间复杂度：O(N·(k+2))，用于存储 best 状态表。
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # best[i][j] = 到达 i 节点，恰好用了 j 次中转的最小花费
        # 最多允许 K+1 次航段，也即最多 K 次中转
        best = [[float('inf')] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        queue = [(0, src, 0)]  # (总价格，当前节点，中转次数)
        res = float('inf')

        while queue:
            cost, u, stops = queue.pop(0)
            if u == dst:
                return cost
            if stops > k:
                continue
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < best[v][stops + 1]:
                    best[v][stops + 1] = new_cost
                    queue.append((new_cost, v, stops + 1))
            queue.sort()

        return -1