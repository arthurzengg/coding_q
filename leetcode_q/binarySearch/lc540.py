class Solution:
    """
    题目给的是一个有序数组，除了一个元素只出现一次，其余元素都出现两次且相邻。
    我们要找到这个唯一的元素，要求时间复杂度 O(log n)，可以用二分法。

    核心规律：
    - 唯一元素会打破数组的成对结构：
        在唯一元素左边，每对元素的第一个下标是偶数；
        在唯一元素右边，每对元素的第一个下标是奇数。
    - 利用这个规律，在二分时根据 mid 的奇偶性和相邻元素的比较，判断唯一元素在左半边还是右半边。

    具体做法：
    1. 初始化左右边界 left = 0, right = n - 1。
    2. 循环条件是 left < right，取 mid = (left + right) // 2。
    3. 如果 mid 是偶数：
        - 如果 nums[mid] == nums[mid + 1]，说明 (mid, mid+1) 是一对，唯一元素在右边，令 left = mid + 1。
        - 否则唯一元素在左边（包含 mid），令 right = mid。
    4. 如果 mid 是奇数：
        - 如果 nums[mid] == nums[mid + 1]，说明唯一元素在左边，令 right = mid。
        - 否则唯一元素在右边，令 left = mid + 1。
    5. 循环结束时，left 指向唯一元素的位置，返回 nums[left]。
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]