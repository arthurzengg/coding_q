class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）算法来找到从原点到目标位置的最小步数。
    2. 由于骑士的移动具有对称性，将目标坐标取绝对值，只考虑第一象限，减少搜索空间。
    3. 定义骑士的八个可能移动方向。
    4. 初始化队列，将起点 (0, 0) 和步数 0 加入队列。
    5. 使用集合记录已访问的位置，避免重复访问。
    6. 在 BFS 循环中，弹出队首元素，检查是否到达目标位置。
    7. 如果未到达目标位置，遍历骑士可以移动到的所有新位置。
    8. 对于每个新位置，检查是否在合理范围内且未被访问过，满足条件则加入队列和已访问集合。
    9. 重复上述过程，直到找到目标位置，返回对应的最小步数。
    """
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(2, 1), (1, 2), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        queue = deque()
        queue.append([0, 0, 0])

        x = abs(x)
        y = abs(y)

        visited = set()
        visited.add((0, 0))

        while queue:
            cur_x, cur_y, step = queue.popleft()
            if cur_x == x and cur_y == y:
                return step
            for dx, dy in directions:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if (next_x, next_y) in visited:
                    continue
                elif next_x < - 1 or next_y < - 1:
                    continue
                else:
                    visited.add((next_x, next_y))
                    queue.append([next_x, next_y, step + 1])