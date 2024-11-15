class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）来更新从每个空地到所有建筑物的最短总距离。
    2. 遍历整个网格，找到所有建筑物的位置，并将它们的位置保存，作为BFS的起始点。
    3. 定义四个可能的移动方向（上、下、左、右）。
    4. 为每个建筑物初始化一个BFS搜索，使用队列来存储需要处理的位置及其当前距离。
    5. 从队列中逐一取出当前位置，并探索其四周的空地（即grid中值为0的位置）。
    6. 如果邻近空地未被当前建筑物的BFS访问过，并且不是障碍物（grid中值为2），则更新该空地到建筑物的距离。
    7. 同时记录每个空地被访问的次数，只有被所有建筑物访问过的空地才被考虑为可能的建房位置。
    8. 在所有BFS完成后，遍历所有空地，找出到所有建筑物的最短总距离最小的空地。
    9. 如果存在这样的空地，返回其最短总距离；否则返回-1，表示没有合适的建房位置。
    """

    def shortestDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        distance = [[float('inf') for _ in range(m)] for _ in range(n)]
        visit_time = [[0 for _ in range(m)] for _ in range(n)]

        buildings = []

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings.append([i, j, 0])
                    distance[i][j] = 0

        for building in buildings:
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[building[0]][building[1]] = True
            queue = deque()
            queue.append(building)

            while queue:
                cur_x, cur_y, step = queue.popleft()

                for dx, dy in directions:
                    next_x = cur_x + dx
                    next_y = cur_y + dy

                    if 0 <= next_x < n and 0 <= next_y < m:
                        if grid[next_x][next_y] != 2 and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            if grid[next_x][next_y] == 0:
                                if distance[next_x][next_y] == float('inf'):
                                    distance[next_x][next_y] = step + 1
                                    queue.append([next_x, next_y, step + 1])
                                else:
                                    distance[next_x][next_y] += step + 1
                                    queue.append([next_x, next_y, step + 1])
                                visit_time[next_x][next_y] += 1

        min_distance = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and distance[i][j] != float('inf') and visit_time[i][j] == len(buildings):
                    min_distance = min(min_distance, distance[i][j])

        return min_distance if min_distance != float('inf') else -1