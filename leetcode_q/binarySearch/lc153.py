class Solution:
    """
    具体实现方法如下：
    1. 初始化左右指针分别指向数组的开始和结束。
    2. 设置一个变量 res 来记录遍历过程中的最小值，初始设置为正无穷。
    3. 使用二分查找方法：
       - 计算中点 mid，并取得该位置的元素值 target。
       - 更新 res，如果 mid 位置的值比当前 res 小，则更新 res。
       - 分析当前的子数组结构，判断旋转的位置：
         - 如果左边界值小于或等于中点值，说明左半部分是有序的。
           - 进一步判断，如果中点值小于或等于右边界值，说明整个数组是有序的，移动右指针到 mid - 1。
           - 否则，左半部分虽有序，但最小值不在其中，移动左指针到 mid + 1。
         - 如果左边界值大于中点值，说明最小值在左半部分，移动右指针到 mid - 1。
    4. 当左指针大于右指针时，结束循环，返回 res。
    """

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            target = nums[mid]
            if target < res:
                res = min(res, target)
            if nums[left] <= nums[mid]:
                if nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid - 1
        return res

