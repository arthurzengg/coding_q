class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        res = 0
        while left < right:
            while nums[left] != nums[right]:
                if nums[left] > nums[right]:
                    res += 1
                    right = right - 1
                    nums[right] += nums[right + 1]
                else:
                    res += 1
                    left = left + 1
                    nums[left] += nums[left - 1]
            left += 1
            right -= 1
        return res

sol = Solution()
print(sol.minimumOperations([4,3,2,1,2,3,1]))
# Output: 2
# Explanation: We can turn the array into a palindrome in 2 operations as follows:
# - Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
# - Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
# The array [4,3,2,3,4] is a palindrome.
# It can be shown that 2 is the minimum number of operations needed.