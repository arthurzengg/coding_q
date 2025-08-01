from collections import defaultdict
import heapq


class Solution:
    """
    - 解法：对每个城市作为起点，使用 Dijkstra 算法计算从该点出发到所有其他城市的最短路径；
    - 统计在 distanceThreshold 范围内可达的城市数量
    - 最后在这些数量中找出最小值，并返回编号最大的下标。
    """

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        res = []
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))
        for node in range(n):
            queue = [(0, node)]
            heapq.heapify(queue)
            dist = [float('inf') for _ in range(n)]
            dist[node] = 0
            while queue:
                w, u = heapq.heappop(queue)
                if dist[u] < w or w > distanceThreshold:
                    continue
                if dist[u] > w:
                    dist[u] = w
                for w_v, v in graph[u]:
                    heapq.heappush(queue, (w + w_v, v))
            cities = 0
            for d in dist:
                if d != float('inf'):
                    cities += 1
            res.append(cities)

        idx = max(i for i, val in enumerate(res) if val == min(res))
        return idx
