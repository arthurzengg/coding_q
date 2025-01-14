class Solution:
    """
    具体思路：
    1. 首先检查数组是否为空，若为空，则直接返回 [-1, -1]。
    2. 使用二分查找方法找到目标值 target 的下界（起始位置）。
       - 定义 findLowerBound 函数来实现这一查找，该函数返回第一个不小于 target 的元素的位置。
    3. 验证找到的位置是否确实是 target，如果不是或者超出数组范围，表明数组中不存在 target，返回 [-1, -1]。
    4. 如果找到 target，则再次调用 findLowerBound 函数查找 target + 1 的下界，并将得到的位置减一，即为 target 的结束位置。
       - 这样做是因为 target + 1 的下界即是 target 的最后一个元素的下一位置。
    5. 返回 target 的起始和结束位置。
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        start = self.findLowerBound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.findLowerBound(nums, target + 1) - 1
        return [start, end]

    def findLowerBound(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left