# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    """
    此解法用于通过 ArrayReader 接口寻找数组的平衡点，即数组可被分为和相等的两部分的位置。
    思路：
    1. 使用二分搜索方法来寻找可能的平衡点。
    2. 通过 ArrayReader 提供的 compareSub 方法比较左右两部分的和。
    3. 根据比较结果调整搜索范围，不断缩小左右边界直到找到平衡点或确认不存在。
    4. 处理奇偶长度的数组，确保正确比较不同情况下的子数组。

    方法：
    - getIndex(reader: 'ArrayReader') -> int: 主函数，利用二分搜索和 ArrayReader 的接口，寻找数组的平衡点。
    """
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left = 0
        right = n - 1

        while left < right:
            if (left + right) % 2 == 1:
                mid = (right + left) // 2
                res = reader.compareSub(left, mid, mid + 1, right)
                if res == 1:
                    right = mid
                elif res == -1:
                    left = mid + 1
            else:
                mid = (right + left) // 2
                res = reader.compareSub(left, mid, mid, right)
                if res == 1:
                    right = mid
                elif res == -1:
                    left = mid
                else:
                    return mid
        return left