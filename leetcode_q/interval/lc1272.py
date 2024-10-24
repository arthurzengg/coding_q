# 解题思路分析：
#
# 本题无非3种情况：
#
# 当删除区间的开始下标在当前区间内时，当前区间开始位置到删除区间开始位置会被分割成一个新的区间
# 当删除区间的结束下标在当前区间内时，删除区间结束位置到当前区间结束位置会被分割成一个新的区间
# 如果当前区间与删除区间没有交集，那么当前区间是一个合理区间。
# 除以上情况之外再无其他可能。

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # 删除区间的开始下标在当前区间内
            if toBeRemoved[0] > interval[0] and toBeRemoved[0] < interval[1]:
                res.append([interval[0], toBeRemoved[0]])
            # 删除区间的结束下标在当前区间内
            if toBeRemoved[1] < interval[1] and toBeRemoved[1] > interval[0]:
                res.append([toBeRemoved[1], interval[1]])
            # 当前区间与删除区间没有交集
            if toBeRemoved[0] >= interval[1] or toBeRemoved[1] <= interval[0]:
                res.append([interval[0], interval[1]])
        return res