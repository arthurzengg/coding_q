from collections import defaultdict

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        n = len(words)
        words.sort(key=len)
        dp = defaultdict(int)
        ans = 0
        for word in words:
            x = 1
            for i in range(len(word)):
                t = word[:i] + word[i + 1:]
                x = max(dp[t] + 1, x)
                # print(x)
            dp[word] = x
            # print(dp)
            ans = max(ans, x)
        return ans

sol = Solution()
print(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]))  # 示例输入