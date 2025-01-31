class Solution:
    """
    中文思路解析：
    1. 如果数组只有一个元素，直接返回这个元素。
    2. 初始化两个动态规划数组 dp_max 和 dp_min，用于存储到当前位置 i 的最大子数组和与最小子数组和。
    3. 对于数组中的每个元素，更新 dp_max 和 dp_min：
       - dp_max[i] 存储到索引 i 的最大子数组和，可由前一个最大子数组和加上当前元素或仅当前元素的较大者得到。
       - dp_min[i] 存储到索引 i 的最小子数组和，可由前一个最小子数组和加上当前元素或仅当前元素的较小者得到。
    4. 如果整个数组的最小子数组和等于数组的总和，说明最小子数组包含了整个数组，此时不能通过减去最小子数组来获取非空子数组，因此返回 dp_max 中的最大值。
    5. 否则，最大环形子数组和可能是 dp_max 中的最大值或是数组总和减去最小子数组和中的较大值。因为最大环形子数组可能是由数组的头部和尾部组成。
    """

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp_max = n * [0]
        dp_min = n * [0]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] + nums[i], nums[i])
            dp_min[i] = min(dp_min[i - 1] + nums[i], nums[i])

        if min(dp_min) == sum(nums):
            # 最小子数组覆盖了整个数组，此时无法通过「总和 - 最小子数组」得到一个有效的“环形”子数组
            return max(dp_max)
        return max(max(dp_max), sum(nums) - min(dp_min))
