class Solution:
    """
    此解法用于计算二维网格中的最大岛屿面积。岛屿由四面相连的 1 表示，被水包围，即由 0 表示。

    思路：
    1. 使用广度优先搜索（BFS）遍历每一个可能的岛屿单元。
    2. 对于每个值为 1 的单元，启动 BFS，将与其相邻的所有 1 单元加入队列，并在遍历过程中标记为 0（避免重复访问）。
    3. 每次 BFS 会得到一块完整岛屿的面积，并与当前最大面积比较，更新结果。
    4. 如果整个网格中没有岛屿，则返回面积为 0。
    """


def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    max_area = 0

    def find_area(i, j, grid):
        queue = [(i, j)]
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        area = 1
        while queue:
            dx, dy = queue.pop()
            grid[dx][dy] = 0
            for nx, ny in directions:
                if 0 <= dx + nx < len(grid) and 0 <= dy + ny < len(grid[0]):
                    if grid[dx + nx][dy + ny] == 1:
                        area += 1
                        grid[dx + nx][dy + ny] = 0
                        queue.append((dx + nx, dy + ny))
        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = find_area(i, j, grid)
                print(area)
                if area > max_area:
                    max_area = area

    return max_area