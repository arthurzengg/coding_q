class Solution:
    """
    思路分析：
    题目要求找出能同时流向太平洋和大西洋的坐标点。水只能从高处向低处或等高处流动。

    暴力法是从每个点出发，判断是否能分别到达两个大洋，但这样会重复计算、效率低，时间复杂度高达 O(m^2 * n^2)。

    因此我们采用反向思路：
    与其从每个点判断能不能流到海洋，不如从海洋边界反过来向内 DFS，
    只走“可以倒流回来的路径”（即当前高度 ≤ 相邻点高度），
    从而找出**哪些点可以流到太平洋**、**哪些点可以流到大西洋**。

    具体做法：
    - 从太平洋边界（上边和左边）出发 DFS，标记所有能倒流回这些边界的点。
    - 同理，从大西洋边界（右边和下边）出发 DFS。
    - 最后找出两个标记矩阵中都为 True 的点，即为答案。

    这样每个点最多被访问两次，时间复杂度为 O(m * n)，是最优解法之一。

    为什么要这样做：
    本质是反向建图，把“能流到海洋”变为“能从海洋走回来”，
    这样可以从少数边界点出发扩展，避免从每个点重复判断，提高效率。
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(heights)
        n = len(heights[0])
        can_reach_pacific = [[False for _ in range(n)] for _ in range(m)]
        can_reach_atlantic = [[False for _ in range(n)] for _ in range(m)]

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(heights, find_border, i, j, prev_height):
            if find_border[i][j] == True:
                return
            find_border[i][j] = True
            for x, y in directions:
                nextx = i + x
                nexty = j + y
                if 0 <= nextx < m and 0 <= nexty < n:
                    if heights[nextx][nexty] >= prev_height:
                        dfs(heights, find_border, nextx, nexty, heights[nextx][nexty])

        for i in range(m):
            dfs(heights, can_reach_pacific, i, 0, heights[i][0])
            dfs(heights, can_reach_atlantic, i, n - 1, heights[i][n - 1])

        for j in range(n):
            dfs(heights, can_reach_pacific, 0, j, heights[0][j])
            dfs(heights, can_reach_atlantic, m - 1, j, heights[m - 1][j])

        for i in range(m):
            for j in range(n):
                if can_reach_atlantic[i][j] == True and can_reach_pacific[i][j] == True:
                    res.append([i, j])
        return res
