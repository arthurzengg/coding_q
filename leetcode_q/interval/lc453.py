class Solution:
    """
    题目要求移除最少的区间，使得剩下的区间互不重叠。

    核心思路（贪心）：
    1. 想要留下最多不重叠的区间，相当于找“最大不重叠区间数”。
    2. 每次选择 **右端点最小的区间**，这样能给后面区间留下更多空间。
    3. 遍历时记录上一个区间的右端点 pre_right，如果新区间的左端点 >= pre_right，
       就说明不重叠，可以保留；否则跳过。
    4. 最终答案 = 总区间数 - 最大不重叠区间数。
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        pre_right = float('-inf')
        max_unoverlapping = 0
        for left, right in intervals:
            if left >= pre_right:
                max_unoverlapping += 1
                pre_right = right
        return len(intervals) - max_unoverlapping