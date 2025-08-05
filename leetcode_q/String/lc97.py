class Solution:
    """
    思路解析：
    本题是经典的字符串交错问题，可以使用二维动态规划解决。
    定义 dp[i][j] 表示 s1 的前 j 个字符 和 s2 的前 i 个字符 能否交错组成 s3 的前 i+j 个字符。

    状态转移方程：
        如果 dp[i][j-1] 为 True，且 s1[j-1] == s3[i+j-1]，说明可以从 s1 中取一个字符匹配 s3，更新 dp[i][j]。
        或者：
        如果 dp[i-1][j] 为 True，且 s2[i-1] == s3[i+j-1]，说明可以从 s2 中取一个字符匹配 s3，更新 dp[i][j]。

    初始化：
        dp[0][0] = True，表示空字符串和空字符串能组成空字符串。
        第一行 dp[0][j] 表示只用 s1 来匹配 s3；
        第一列 dp[i][0] 表示只用 s2 来匹配 s3。

    时间复杂度：O(m * n)
    空间复杂度：O(m * n)
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len:
            return False
        dp = [[False for _ in range(s1_len + 1)] for _ in range(s2_len + 1)]
        dp[0][0] = True

        for i in range(1, s2_len + 1):
            dp[i][0] = (dp[i - 1][0] and s2[i - 1] == s3[i - 1])

        for j in range(1, s1_len + 1):
            dp[0][j] = (dp[0][j - 1] and s1[j - 1] == s3[j - 1])

        for i in range(1, s2_len + 1):
            for j in range(1, s1_len + 1):
                dp[i][j] = (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]) or (
                            dp[i - 1][j] and s2[i - 1] == s3[i + j - 1])

        return dp[-1][-1]

