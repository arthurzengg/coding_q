def calculateWays(wordLen, maxVowels):
    MOD = 10 ** 9 + 7
    # If maxVowels >= wordLen, there is no restriction
    if maxVowels >= wordLen:
        return pow(26, wordLen, MOD)

    dp = [[0] * (maxVowels + 1) for _ in range(wordLen + 1)]
    dp[0][0] = 1

    for pos in range(1, wordLen + 1):
        # Ways to end with a consonant
        total_prev = sum(dp[pos - 1]) % MOD
        dp[pos][0] = (total_prev * 21) % MOD
        # Ways to end with cv consecutive vowels
        for cv in range(1, maxVowels + 1):
            dp[pos][cv] = (dp[pos - 1][cv - 1] * 5) % MOD

    total_ways = sum(dp[wordLen]) % MOD
    return total_ways


# Test cases
print(calculateWays(2, 1))  # wordLen = 1, maxVowels = 1, expect 26
print(calculateWays(2, 2))  # wordLen = 4, maxVowels = 1, should match detailed explanation
print(calculateWays(2, 0))  # wordLen = 4, maxVowels = 2, should match detailed explanation
