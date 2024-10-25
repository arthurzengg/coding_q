class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # 获取房子的总数
        n = len(costs)
        # 如果只有一座房子，直接返回三种颜色中最小的成本
        if n == 1:
            return min(costs[0])
        # 初始化动态规划数组，所有值设为无穷大
        dp = [[float('inf') for _ in range(3)] for _ in range(n)]
        # 设置第一座房子涂三种颜色的初始成本
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        # 从第二座房子开始计算每座房子的最小涂色成本
        for i in range(1, n, 1):
            # 计算涂第i座房子为红色的最小成本
            dp[i][0] = min(dp[i - 1][1] + costs[i][0], dp[i - 1][2] + costs[i][0])
            # 计算涂第i座房子为蓝色的最小成本
            dp[i][1] = min(dp[i - 1][0] + costs[i][1], dp[i - 1][2] + costs[i][1])
            # 计算涂第i座房子为绿色的最小成本
            dp[i][2] = min(dp[i - 1][0] + costs[i][2], dp[i - 1][1] + costs[i][2])

        # 返回最后一座房子的最小涂色成本
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])