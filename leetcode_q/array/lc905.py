class Solution:
    """
    思路解析：
    遍历数组，如果遇到偶数，就取出它并插入到数组开头。
    时间复杂度：O(n^2)
    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                even = nums.pop(i)
                nums.insert(0, even)
        return nums
