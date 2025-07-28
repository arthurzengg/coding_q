class Solution:
    """
    思路：
    - 使用滑动窗口（双指针）方法解决。
    - 用两个指针 left 和 right 表示窗口的左右边界。
    - 当窗口中 0 的数量不超过 k 时，继续向右扩展窗口；
    - 一旦 0 的数量超过 k，说明窗口不合法，收缩左边界直到合法。
    - 每次右指针移动后，更新当前合法窗口的最大长度。

    变量说明：
    - left：窗口左边界
    - right：窗口右边界
    - k_count：当前窗口中 0 的数量（也就是需要被翻转的 0）
    - res：记录所有合法窗口中最长的长度
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        res = 0
        k_count = 0
        while right < n:
            if nums[right] == 0:
                k_count += 1
                while k_count > k:
                    if nums[left] == 0:
                        left += 1
                        k_count -= 1
                    else:
                        left += 1
                right += 1
                res = max(res, right - left)
            else:
                right += 1
                res = max(res, right - left)
        return res

