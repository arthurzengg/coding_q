class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # 辅助函数，用于计算在选择当前颜色j时，前一个房子可以选择的最小成本
        def find_min_dp(i, j, costs, color, dp):
            color = [i for i in range(color)]  # 生成一个包含所有颜色索引的列表
            color.remove(j)  # 移除当前颜色，以防止同色相邻
            cost_list = []
            for c in color:
                cost_list.append(dp[i - 1][c] + costs[i][j])  # 计算选择每种不同颜色的成本，并加上当前颜色的成本
            return min(cost_list)  # 返回最小成本

        n = len(costs)  # 房子的数量
        color = len(costs[0])  # 可选的颜色数量
        if n == 1:
            return min(costs[0])  # 如果只有一个房子，直接返回最小成本

        # 初始化动态规划表
        dp = [[0 for _ in range(color)] for _ in range(n)]

        # 初始化第一个房子的成本
        for i in range(color):
            dp[0][i] = costs[0][i]

        # 填充动态规划表
        for i in range(1, n):
            for j in range(color):
                dp[i][j] = find_min_dp(i, j, costs, color, dp)  # 计算每种颜色的最小成本

        # 收集最后一个房子每种颜色的成本
        res = []
        for i in range(color):
            res.append(dp[n - 1][i])

        # 返回最终的最小成本
        return min(res)