class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）来更新每个房间到最近门的距离。
    2. 先遍历整个网格，找到所有门的位置，并将这些门的位置作为BFS的起始点加入队列。
    3. 定义四个可能的移动方向（上、下、左、右）。
    4. 从队列中逐一取出当前位置，并探索其四周的房间。
    5. 如果邻近房间是未更新过的房间（值为2147483647），则计算从当前房间到此房间的距离，更新房间的值。
    6. 将更新后的房间位置加入队列，以便进一步探索其邻近房间。
    7. 重复上述过程，直到队列为空。
    8. 通过这种方式，可以确保每个房间的值被更新为到最近门的最短距离。
    """

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n = len(rooms)
        m = len(rooms[0])
        queue = deque()

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append([i, j, 0])

        while queue:
            cur_x, cur_y, step = queue.popleft()
            for dx, dy in directions:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if 0 <= next_x < n and 0 <= next_y < m and rooms[next_x][next_y] == 2147483647:
                    if rooms[cur_x][cur_y] + 1 < rooms[next_x][next_y]:
                        rooms[next_x][next_y] = rooms[cur_x][cur_y] + 1
                        queue.append([next_x, next_y, rooms[cur_x][cur_y] + 1])