class Solution:
    """
    解法采用排序 + 双指针的方式，具体步骤如下：

    1. 对数组进行排序，方便后续使用双指针策略；
    2. 固定第一个数 nums[i]，然后设置两个指针：
    - left = i + 1，从左往右；
    - right = n - 1，从右往左；
    三个数相加后判断与 target 的距离；
    3. 如果当前三数之和更接近目标值，就更新最接近值 `ans`；
    4. 如果当前和大于 target，说明需要更小的值，因此 `right -= 1`；
    如果当前和小于或等于 target，说明需要更大的值，因此 `left += 1`；
    5. 过程中的 `if i > 0 and nums[i] == nums[i - 1]` 是为了跳过重复的首位元素，虽然本题不要求返回所有组合，但这有助于减少重复判断；
    6. 最终返回记录下的最接近 target 的三数之和。

    时间复杂度：O(n²)，因为外层循环 O(n)，内层双指针 O(n)
    空间复杂度：O(1)，原地排序 + 常数空间
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        abs_diff = float('inf')
        nums.sort()
        ans = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: #避免重复计算首位元素
                continue
            left = i + 1
            right = n - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if abs(res - target) < abs_diff:
                    abs_diff = abs(res - target)
                    ans = res
                if res > target:
                    right -= 1
                else:
                    left += 1
        return ans
