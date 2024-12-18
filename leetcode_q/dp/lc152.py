class Solution:
    """
    此解法用于找出数组中子数组的最大乘积。
    思路：
    1. 使用动态规划的思想，维护两个变量 max_possible 和 min_possible 来分别记录到当前位置为止，包含当前元素的最大乘积和最小乘积。
       - max_possible 是以当前元素结尾的子数组的最大乘积。
       - min_possible 是以当前元素结尾的子数组的最小乘积（这个值是负的时候特别有用，因为一个负数乘以一个负的最小值可以变成最大值）。
    2. 对于数组中的每一个元素 nums[i]，基于前一个元素更新 max_possible 和 min_possible。
       - 新的 max_possible 是当前元素 nums[i] 和前一状态的 max_possible * nums[i]、min_possible * nums[i] 三者中的最大值。
       - 新的 min_possible 是当前元素 nums[i] 和前一状态的 max_possible * nums[i]、min_possible * nums[i] 三者中的最小值。
    3. 使用一个变量 res 来跟踪和更新遇到的最大 max_possible。
    4. 最终，res 中存储的是全局的最大乘积。

    方法：
    - maxProduct(nums): 输入一个整数数组 nums，返回该数组中子数组的最大乘积。
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_possible = nums[0]
        min_possible = nums[0]
        res = nums[0]

        for i in range(1, n):
            temp_max = max_possible
            max_possible = max(nums[i], temp_max * nums[i], min_possible * nums[i])
            min_possible = min(nums[i], temp_max * nums[i], min_possible * nums[i])
            res = max(res, max_possible)

        return res