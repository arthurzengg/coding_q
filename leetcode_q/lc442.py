# 这题的关键点在于1 <= nums[i] <= n
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res

sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
# output is [2, 3]