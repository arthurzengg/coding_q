M = 1000000007

def add(x, y):
    x += y
    if x >= M:
        x -= M
    return x

def mul(x, y):
    return int(x * y % M)

def getZ(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i <= right and z[i - left] <= right - i:
            z[i] = z[i - left]
        else:
            z_i = max(0, right - i + 1)
            while i + z_i < n and s[i + z_i] == s[z_i]:
                z_i += 1
            z[i] = z_i
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    return z

def matrixMultiply(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    r = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                r[i][j] = add(r[i][j], mul(a[i][k], b[k][j]))
    return r

def matrixPower(a, y):
    n = len(a)
    r = [[0] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 1
    x = [a[i][:] for i in range(n)]
    while y > 0:
        if y & 1:
            r = matrixMultiply(r, x)
        x = matrixMultiply(x, x)
        y >>= 1
    return r

def getNumWays(src, target, k):
    n = len(src)
    dp = matrixPower([[0, 1], [n - 1, n - 2]], k)[0]
    src += target + target
    z = getZ(src)
    m = n + n
    result = 0
    for i in range(n, m):
        if z[i] >= n:
            result = add(result, dp[0] if i - n == 0 else dp[1])
    return result

print(getNumWays("abcd", "cdab", 2))
print(getNumWays("ababab", "ababab", 1))
print(getNumWays("aaaa", "aaaa", 2))