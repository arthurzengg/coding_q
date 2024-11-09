class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）来探索从起点到终点的路径。
    2. 创建一个方向数组，用于确定每个位置可以沿四个方向移动（上下左右）。
    3. 使用一个集合seen记录已访问的位置，以避免重复访问。
    4. 将起点加入队列queue，并初始化探索。
    5. 对于每一个位置，沿每个方向不停移动，直到碰到墙壁或边界，然后检查该位置是否到达终点或未访问。
    6. 如果到达终点，则返回True；否则，将新位置加入队列继续探索。
    7. 如果队列为空仍未找到路径，则返回False，表示不存在到达终点的路径。
    """

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n = len(maze)
        m = len(maze[0])

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        seen = {tuple(start)}

        queue = deque()
        queue.append(start)

        while queue:
            y, x = queue.popleft()
            for dx, dy in direction:
                cury = y
                curx = x
                while 0 <= dx + curx < m and 0 <= dy + cury < n and maze[dy + cury][dx + curx] != 1:
                    curx += dx
                    cury += dy
                if (cury, curx) in seen:
                    continue
                elif [cury, curx] == destination:
                    return True
                else:
                    queue.append((cury, curx))
                    seen.add((cury, curx))
        return False