class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        targetNums = 0
        i = left
        while i < n:
            if nums[i] == target:
                targetNums += 1
            i += 1
        return targetNums > n / 2