class Solution:
    """
    贪心算法求解射爆气球的最少箭数。
    思路：
    1. 先将所有气球按照起始坐标排序。
    2. 初始化射箭次数为0，cur记录当前可以合并的最大气球区间。
    3. 遍历排序后的气球列表，判断当前气球是否能与cur合并：
       - 如果能合并，则更新cur为当前区间与cur的交集，这表示当前箭可以同时射爆这些气球。
       - 如果不能合并，意味着需要一支新的箭，更新cur为当前气球的区间，并且射箭次数加一。
    4. 遍历结束后，返回射箭次数，因为最后一个区间需要加上一箭。
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)

        if n == 1:
            return 1

        ans = 0

        cur = [points[0]]

        for i in range(1, n):
            if points[i][0] <= cur[-1][1]:
                cur = [[max(points[i][0], cur[-1][0]), min(points[i][1], cur[-1][1])]]
            else:
                cur = [points[i]]
                ans += 1
        return ans + 1