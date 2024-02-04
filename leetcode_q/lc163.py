class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        res = [] 
        next_expected = lower  # 设置下一个期望的数字为下界lower

        for num in nums:  # 遍历输入的有序数组nums
            if num == next_expected:  # 如果当前数字等于期望的数字
                next_expected += 1  # 更新下一个期望的数字
                continue  # 继续检查下一个数字

            # 如果当前数字大于期望的数字，说明有缺失的区间
            if next_expected == num - 1:  # 如果缺失的区间只有一个数字
                res.append([next_expected, next_expected])  # 将这个单独的数字作为一个区间添加到结果列表中
            else:  # 如果缺失的区间包含多个数字
                res.append([next_expected, num - 1])  # 将缺失的区间添加到结果列表中
            next_expected = num + 1  # 更新下一个期望的数字为当前数字加一

        # 遍历结束后，检查是否有从最后一个数字到上界upper的缺失区间
        if next_expected <= upper:  # 如果还有剩余的区间
            if next_expected == upper:  # 如果剩余的区间只包含一个数字
                res.append([next_expected, next_expected])
            else:
                res.append([next_expected, upper])

        return res

sol = Solution()
print(sol.findMissingRanges([0,1,3,50,75], 0, 99))
# Output: [[2, 2], [4, 49], [51, 74], [76, 99]]

# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]

