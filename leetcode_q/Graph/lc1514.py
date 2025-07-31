from collections import defaultdict
import heapq


class Solution:
    """
    这是一个变种的 Dijkstra 算法问题。不同点是：
    - Dijkstra 中求的是**最短路径（权重最小）**，而本题求的是**最大概率路径（权重最大）**
    - 因为要找乘积最大的路径，所以我们每次在堆中取出的是**当前概率最大的路径**

    具体思路：
    1. 建图：用 `graph[u].append([p, v])` 方式记录每条边的概率。
    2. 使用一个优先队列（最大堆）来进行贪心地选择概率最大的路径；
       - 注意：Python 默认是最小堆，因此我们把概率取负值来模拟最大堆。
    3. 用 `dist[i]` 记录从起点到 `i` 的最大成功概率；
    4. 每次从堆中取出一个点 `node`，如果是旧路径（`weight < dist[node]`），跳过；
    5. 遍历其邻居，计算通过该节点能否获得更高的概率，如果可以则更新并入堆；
    6. 最后返回 `dist[end_node]` 即为最大成功概率。

    时间复杂度为 O(E log V)，适用于中等规模的图。
    """

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append([p, v])
            graph[v].append([p, u])
        dist = [0 for _ in range(n)]
        dist[start_node] = 1
        queue = [(-1, start_node)]
        heapq.heapify(queue)
        while queue:
            weight, node = heapq.heappop(queue)
            weight = -weight
            if weight < dist[node]:  # 时如果不加判断，就会用旧路径覆盖最优路径，破坏正确性
                continue
            for weight_neighbor, neighbor in graph[node]:
                print(weight_neighbor, neighbor)
                total_weight = weight * weight_neighbor
                if total_weight > dist[neighbor]:
                    dist[neighbor] = total_weight
                    heapq.heappush(queue, (-total_weight, neighbor))
        return dist[end_node]

