class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 获取网格的行数和列数
        rows = len(grid)
        cols = len(grid[0])
        # 初始化腐烂橘子的位置列表和新鲜橘子的数量
        rotten = []
        fresh = 0

        # 遍历网格，统计新鲜橘子的数量并记录腐烂橘子的位置
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        # 初始化用来计算腐烂所需时间的分钟数
        minutes = 0
        # 四个可能的移动方向
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 当还有腐烂橘子和新鲜橘子时，循环继续
        while rotten and fresh > 0:
            # 增加分钟数
            minutes += 1
            # 对当前所有的腐烂橘子进行遍历
            for _ in range(len(rotten)):
                # 弹出腐烂橘子的位置
                r, c = rotten.pop(0)
                # 检查腐烂橘子四周的橘子是否新鲜
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 如果新鲜，让它腐烂并加入列表
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))

        # 如果没有新鲜橘子剩余，返回所需的分钟数；否则返回-1
        if fresh == 0:
            return minutes
        else:
            return -1

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
# Output: 4