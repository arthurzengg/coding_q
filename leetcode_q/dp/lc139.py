class Solution:
    """
    中文思路解析：
    1. 定义一个长度为 n+1 的布尔数组 dp，其中 n 是字符串 s 的长度。dp[i] 表示 s 的前 i 个字符是否可以被完全分割。
    2. 初始化 dp[0] 为 True，因为空字符串总是可以被表示。
    3. 遍历字符串 s 的每一个子串长度 i 从 1 到 n：
       - 对于每个长度 i，再遍历字典 wordDict 中的每个单词 word：
         - 如果当前子串长度大于等于单词长度，并且 dp[i - len(word)] 为 True（表示 s 的前 i-len(word) 个字符可以被完全分割），
           且 s 从 i-len(word) 到 i 的子串正好等于 word，那么将 dp[i] 设置为 True。
    4. 最后，返回 dp[n]，它表示整个字符串 s 是否可以被完全分割。
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(len(wordDict)):
                if i >= len(wordDict[j]):
                    if dp[i - len(wordDict[j])] and s[i - len(wordDict[j]):i] == wordDict[j]:
                        dp[i] = True
        return dp[n]