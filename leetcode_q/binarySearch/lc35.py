class Solution:
    # 左闭右闭区间写法
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left

    # 左闭右开区间写法
    def lower_bound2(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # 左闭右开区间 [left, right) 因为不包含right，但同时又要计算nums[-1]，就只能这样
        while left < right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right] >= target
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # 范围缩小到 [mid+1, right)
            else:
                right = mid  # 范围缩小到 [left, mid)
        return left  # 或者 right

