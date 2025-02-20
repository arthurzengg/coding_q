# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
    中文思路解析：
    这个函数用于猜测一个从 1 到 n 范围内的数字。通过调用预定义的 guess API 来比较你的猜测数字与实际的目标数字。

    具体实现方法如下：
    1. 判断 n 是否为 1，如果为 1，则直接返回 1。
    2. 使用二分查找的方法来优化猜数字的过程。
       - 初始化左右边界，left 设置为 1，right 设置为 n。
       - 在 left 小于 right 的条件下，计算中间值 mid。
       - 使用 guess(mid) 来判断 mid 与目标数字的关系：
         - 如果 guess(mid) 返回 0，说明 mid 是目标数字，直接返回 mid。
         - 如果 guess(mid) 返回 -1，说明目标数字小于 mid，调整右边界 right 到 mid。
         - 如果 guess(mid) 返回 1，说明目标数字大于 mid，调整左边界 left 到 mid + 1。
    3. 当 left 等于 right，结束循环，此时 left（或 right）即为猜测的数字。

    关键点：
    - 通过二分查找减少猜测次数，每次猜测都基于 guess 函数的反馈调整搜索范围。
    - 正确处理二分查找的边界和中点计算，确保不会出现无限循环或者错过正确答案。
    """

    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid
            else:
                left = mid + 1
        return left