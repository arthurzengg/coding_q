class Solution:
    """
    # 思路：
    1. 使用 Dijkstra 算法（优先队列）来找到从球到洞的最短路径，同时考虑路径的字典序。
    2. 创建一个方向数组，包含四个方向（右、左、下、上）及其对应的移动字符（'r'、'l'、'd'、'u'）。
    3. 初始化一个三维数组 dis，用于记录到达每个位置的最短距离和对应的路径。
    4. 将初始位置和路径加入最小堆 heap 中，开始搜索。
    5. 当堆不为空时，弹出堆顶元素，获取当前位置和路径。
    6. 如果当前位置是洞的位置，返回当前路径。
    7. 对于每个方向，滚动球直到碰到墙壁、边界或到达洞，记录滚动的距离和路径。
    8. 如果新位置的距离更短，或者距离相同但路径字典序更小，更新 dis 数组，并将新状态加入堆中。
    9. 如果遍历完所有可能的路径仍未到达洞的位置，返回 "impossible"。
    """

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])

        direction = [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]
        dis = [[[float('inf'), ''] for _ in range(n)] for _ in range(m)]
        dis[ball[0]][ball[1]][0] = 0

        heap = [[0, '', ball[0], ball[1]]]
        heapq.heapify(heap)

        while heap:
            cur = heapq.heappop(heap)
            path = cur[1]
            cur_x = cur[2]
            cur_y = cur[3]

            if [cur_x, cur_y] == hole:
                return path

            for dx, dy, d in direction:
                count = 0
                x = cur_x
                y = cur_y
                temp_path = path
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    count += 1
                    if [x, y] == hole:
                        break
                temp_path += d

                if dis[cur_x][cur_y][0] + count < dis[x][y][0] or (
                        dis[cur_x][cur_y][0] + count == dis[x][y][0] and temp_path < dis[x][y][1]):
                    dis[x][y][0] = dis[cur_x][cur_y][0] + count
                    dis[x][y][1] = temp_path
                    heapq.heappush(heap, [dis[x][y][0], temp_path, x, y])
        return 'impossible'


