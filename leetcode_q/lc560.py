from collections import defaultdict
class Solution:
    # 方法一 前缀和
    # 我们先遍历一次数组，求出前缀和数组。之后这个数组可以代替我们最开始暴力解法的sumsumsum函数。但是很遗憾，这种做法复杂度还是O(n ^ 2)
    # def subarraySum(self, nums: list[int], k: int) -> int:
    #     # 要求的连续子数组
    #     count = 0
    #     n = len(nums)
    #
    #     preSum = [0]
    #
    #     # 求前缀和数组
    #     tmp = 0
    #     for i in range(n):
    #         tmp += nums[i]
    #         preSum.append(tmp)
    #
    #     for i in range(1, n + 1):
    #         for j in range(i, n + 1):
    #             if preSum[j] - preSum[i - 1] == k:
    #                 count += 1
    #     return count

    # 方法二 前缀和优化
    def subarraySum(self, nums: list[int], k: int) -> int:

        # 要求的连续子数组
        count = 0
        n = len(nums)

        preSum = [0]

        # 求前缀和数组
        tmp = 0
        for i in range(n):
            tmp += nums[i]
            preSum.append(tmp)

        preSum_dict = defaultdict(int)
        preSum_dict[0] = 1

        # Iterate over the prefix sum array
        for sum_i in preSum[1:]:
            # If there is a prefix sum that, when subtracted from sum_i,
            # results in k, then a subarray summing to k ends at this index
            count += preSum_dict[sum_i - k]
            # Update the count for the current prefix sum
            preSum_dict[sum_i] += 1

        return count

sol = Solution()
print(sol.subarraySum([3,4,7,2,-3,1,4,2], 7))
# Output = 4