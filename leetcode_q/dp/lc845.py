class Solution:
    """
    求数组中“山脉子数组”的最大长度。山脉必须先严格上升再严格下降，长度至少 3。

    做法（双向 DP）：
    1) dp_left_right[i]：以 i 结尾的“严格上升”序列长度（单调上升长度）。
       从左到右扫，若 arr[i] > arr[i-1]，则 dp[i] = dp[i-1] + 1，否则为 1。
    2) dp_right_left[i]：以 i 开始的“严格下降”序列长度（单调下降长度）。
       从右到左扫，若 arr[i] > arr[i+1]，则 dp[i] = dp[i+1] + 1，否则为 1。
    3) 枚举每个 i，若它既有上升也有下降（两边长度都 > 1），
       则以 i 为峰的山脉长度为 dp_left_right[i] + dp_right_left[i] - 1（峰被双计需减 1）。
    4) 取最大值即可。若不存在合法山脉返回 0。

    复杂度：时间 O(n)，空间 O(n)。
    """

    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        if n <= 2:
            return 0
        dp_left_right = [1 for _ in range(n)]
        dp_right_left = [1 for _ in range(n)]

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                dp_left_right[i] = max(dp_left_right[i], dp_left_right[i - 1] + 1)

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                dp_right_left[i] = max(dp_right_left[i], dp_right_left[i + 1] + 1)

        for i in range(n):
            if dp_left_right[i] > 1 and dp_right_left[i] > 1:
                res = max(res, dp_left_right[i] + dp_right_left[i] - 1)
        return res
