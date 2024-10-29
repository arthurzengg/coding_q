from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)  # 迷宫的行数
        n = len(maze[0])  # 迷宫的列数
        # 初始化距离数组，所有值设为无穷大
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        # 设置起始点的距离为0
        distance[start[0]][start[1]] = 0
        # 方向数组，分别表示向下、向上、向右、向左移动
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # 使用队列实现广度优先搜索
        queue = deque()
        queue.append(start)

        # 当队列不为空时，继续循环
        while queue:
            cur = queue.popleft()  # 取出队列的第一个元素

            # 遍历每个可能的方向
            for dir in directions:
                x = cur[0]
                y = cur[1]
                count = 0  # 用于记录从当前点移动到下一个点的距离
                # 检查在当前方向上移动是否越界，以及是否为可通行路径
                while x + dir[0] >= 0 and x + dir[0] < m and y + dir[1] >= 0 and y + dir[1] < n and maze[x + dir[0]][y + dir[1]] == 0:
                    x += dir[0]
                    y += dir[1]
                    count += 1  # 累计移动的距离
                # 更新到达新位置的最短距离
                if distance[cur[0]][cur[1]] + count < distance[x][y]:
                    queue.append([x, y])  # 将新位置加入队列
                    distance[x][y] = distance[cur[0]][cur[1]] + count  # 更新距离

        # 检查是否能到达目的地，并返回最短距离
        if distance[destination[0]][destination[1]] != float('inf'):
            return distance[destination[0]][destination[1]]
        else:
            return -1  # 如果到达不了目的地，返回-1