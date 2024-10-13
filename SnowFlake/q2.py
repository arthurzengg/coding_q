def countPrimeStrings(s):
    MOD = 10 ** 9 + 7
    n = len(s)

    # Precompute all primes up to 10^6
    MAX_PRIME = 10 ** 6 + 1
    is_prime = [True] * MAX_PRIME
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_PRIME ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_PRIME, i):
                is_prime[j] = False
    primes = set(i for i, val in enumerate(is_prime) if val)

    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way

    for i in range(1, n + 1):
        # Only need to consider substrings of length up to 6
        for l in range(1, min(7, i + 1)):
            j = i - l
            if s[j] == '0':
                continue  # No leading zeros
            num = int(s[j:i])
            if num in primes:
                dp[i] = (dp[i] + dp[j]) % MOD

    return dp[n]


print(countPrimeStrings("11375"))
print(countPrimeStrings("3175"))
print(countPrimeStrings("24"))