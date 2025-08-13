class Solution:
    """
    本题是两名玩家轮流从数组两端取数，双方都采取最优策略，问先手是否至少不输（赢或平）。

    关键建模（净胜分 DP）：
    定义 dp[i][j] 表示在子数组 nums[i..j] 上，当前回合玩家相对对手能获得的最大“净胜分”
    （= 当前玩家总分 - 对手总分）。这样把对手的最优反制自然体现在转移式的减号里。

    状态转移：
      - 若当前玩家取左端 nums[i]，之后轮到对手在区间 [i+1..j] 继续最优对弈，
        对手在该区间的最大净胜分为 dp[i+1][j]（注意是对手相对当前玩家的净胜分），
        因此当前玩家本次选择的净胜分：pick_i = nums[i] - dp[i+1][j]
      - 若当前玩家取右端 nums[j]，同理：pick_j = nums[j] - dp[i][j-1]
      - 取二者较大：dp[i][j] = max(pick_i, pick_j)

    边界条件：
      - 当 i == j 时，只有一个数，当前玩家直接拿走：dp[i][i] = nums[i]

    目标答案：
      - 先手在整段 nums[0..n-1] 的最大净胜分为 dp[0][n-1]
      - 若 dp[0][n-1] >= 0，说明先手至少不输（赢或平），返回 True，否则 False

    复杂度：
      - 时间 O(n^2)，空间 O(n^2)
      - 填表顺序：i 从大到小，j 从小到大，保证子问题已计算
    """

    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                pick_i = nums[i] - dp[i + 1][j]
                pick_j = nums[j] - dp[i][j - 1]
                dp[i][j] = max(pick_i, pick_j)

        return dp[0][n - 1] >= 0