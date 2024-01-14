class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        # 定义向左移动直到撞墙的函数
        def go_left(maze, start):
            y, x = start
            while x > 0 and maze[y][x - 1] != 1:  # 检查左边是否为墙
                x -= 1  # 向左移动
            return [y, x]  # 返回新的位置

        # 定义向右移动直到撞墙的函数
        def go_right(maze, start):
            y, x = start
            while x < len(maze[0]) - 1 and maze[y][x + 1] != 1:  # 检查右边是否为墙
                x += 1  # 向右移动
            return [y, x]  # 返回新的位置

        # 定义向上移动直到撞墙的函数
        def go_up(maze, start):
            y, x = start
            while y > 0 and maze[y - 1][x] != 1:  # 检查上方是否为墙
                y -= 1  # 向上移动
            return [y, x]  # 返回新的位置

        # 定义向下移动直到撞墙的函数
        def go_down(maze, start):
            y, x = start
            while y < len(maze) - 1 and maze[y + 1][x] != 1:  # 检查下方是否为墙
                y += 1  # 向下移动
            return [y, x]  # 返回新的位置

        # 使用深度优先搜索来找出是否存在到达目的地的路径
        def dfs(maze, start, destination, seen):
            if start == destination:  # 检查是否到达目的地
                return True
            if tuple(start) in seen:  # 检查当前位置是否已访问
                return False
            seen.add(tuple(start))  # 将当前位置添加到已访问集合

            # 探索所有可能的移动方向
            for next_start in [go_left(maze, start), go_right(maze, start), go_up(maze, start), go_down(maze, start)]:
                if dfs(maze, next_start, destination, seen):  # 递归搜索
                    return True
            return False

        return dfs(maze, start, destination, set())  # 从起点开始搜索

# 示例
sol = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
print(sol.hasPath(maze, [0, 4], [4, 4]))  # 示例输入
