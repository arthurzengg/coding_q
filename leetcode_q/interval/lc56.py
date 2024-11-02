class Solution:
    """
    思路解析：
    这个函数用于合并给定列表中的所有重叠区间。具体步骤如下：
    1. 首先对输入的区间列表按照每个区间的起始位置进行排序。
    2. 创建一个结果列表，初始包含排序后的第一个区间。
    3. 遍历排序后的区间列表，从第二个区间开始比较。
    4. 对于每个区间，如果它的起始位置小于或等于结果列表中最后一个区间的结束位置，说明有重叠：
        - 如果当前区间的结束位置大于结果列表中最后一个区间的结束位置，更新结果列表中最后一个区间的结束位置。
        - 否则，继续检查下一个区间。
    5. 如果当前区间的起始位置大于结果列表中最后一个区间的结束位置，直接将当前区间加入结果列表。
    6. 完成所有区间的检查后，返回结果列表，其中包含了合并后的所有不重叠区间。
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]
        if n == 1:
            return intervals
        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                if intervals[i][1] >= ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
                else:
                    continue
            else:
                ans.append(intervals[i])
        return ans