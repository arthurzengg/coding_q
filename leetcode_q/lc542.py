# 解析：
# 1. 动态规划
# 为了确保每个元素考虑到所有方向上的最近的0，通常需要两次遍历：
#
# 第一次遍历（从左上到右下）确保每个元素与其左侧和上方的0的最短距离被考虑。
# 第二次遍历（从右下到左上）确保每个元素与其右侧和下方的0的最短距离被考虑。
# 这种方法确保了所有方向上最近的0都被考虑进来，从而得到准确的结果。
#
# 如果你试图只用一次遍历，就可能会漏掉某些方向上的最近的0。
# 因此，为了得到正确且可靠的解决方案，两次遍历是必要的。


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        print(dp)

        # 第一次遍历，从左上到右下
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # print(dp)

        # 第二次遍历，从右下到左上
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        # print(dp)

        return dp

sol = Solution()
print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
# Output: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]