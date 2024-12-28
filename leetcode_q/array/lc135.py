class Solution:
    """
    贪心算法
    解析：
    1. 分两种情况
        1. 右边的评分比左边高
        2. 左边的评分比右边高
    2. 上面的这两种遍历顺序是不一样的，如果是一样的话，就不能利用之前的结果
    3. candy[j] = max(candy[j + 1] + 1, candy[j])这步的意思是，既要比左边多也要比右边多
    """

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1 for i in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = candy[j + 1] + 1
        return sum(candy)