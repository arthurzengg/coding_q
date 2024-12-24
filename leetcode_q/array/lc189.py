class Solution:
    """
    此解法用于将数组中的元素向右旋转 k 次。
    思路：
    1. 首先处理 k 的值，使其不超过数组长度 n。因为向右旋转 n 次相当于没有旋转，所以使用 k = k % n 来确保 k 的有效性。
    2. 切片数组，将数组从 n-k 的位置切分为两部分：
       - left 为数组的后 k 个元素，即旋转后应该位于数组前部的元素。
       - right 为前 n-k 个元素，即旋转后应该位于数组后部的元素。
    3. 先将 left 中的元素复制到 nums 的前部，然后将 right 中的元素复制到 nums 的后部。

    方法：
    - rotate(nums, k): 输入数组 nums 和整数 k，原地修改数组，实现右旋转 k 次。
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        left = nums[n - k:]
        right = nums[:n - k]
        for i in range(len(left)):
            nums[i] = left[i]
        for j in range(len(left), n):
            nums[j] = right[j - len(left)]

