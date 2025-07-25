class Solution:
    """
    动态规划思路：
    dp[i][j] 表示字符串 s[i...j] 中的最长回文子序列长度
    状态转移：
    - 如果 s[i] == s[j]：dp[i][j] = dp[i + 1][j - 1] + 2
    - 否则：dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    遍历顺序：i 从 n-1 到 0，j 从 i+1 到 n-1
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1  # 单个字符是回文

        # 反向遍历 i，正向遍历 j
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]