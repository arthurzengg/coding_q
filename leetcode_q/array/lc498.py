class Solution:
    """
    思路解析：
    1. 定义递归函数 traverse(x, y, tmp)，从起点 (x, y) 沿 ↗ 方向（行 -1，列 +1）
       不断收集对角线上的元素到临时列表 tmp，直到越界停止。
    2. 对角线起点分两部分：
       - 前 m-1 条对角线起点在第一列：(i, 0)，i 从 0 遍历到 m-2。
       - 最后一行的对角线起点在最后一行：(m-1, j)，j 从 0 遍历到 n-1。
    3. 收集完一条对角线后，根据起点的行号 i 和列号 j 的奇偶性分别执行一次翻转：
       - if i % 2 == 1: 翻转一次
       - if j % 2 == 1: 再翻转一次
       这样只有当 i 和 j 恰好有一个为奇数时，tmp 会被翻转一次，满足「对角线编号 k = i+j 为奇数时翻转」的要求。
    4. 将处理好的 tmp 拼接到结果列表 res 中，依次遍历所有对角线即可。
    """

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []

        def traverse(x, y, tmp):
            if not 0 <= x < m or not 0 <= y < n:
                return
            tmp.append(mat[x][y])
            traverse(x - 1, y + 1, tmp)

        for i in range(m):
            if i == m - 1:
                for j in range(n):
                    tmp = []
                    traverse(m - 1, j, tmp)
                    if i % 2 == 1:
                        tmp = tmp[::-1]
                    if j % 2 == 1:
                        tmp = tmp[::-1]
                    res += tmp[:]
            else:
                tmp = []
                traverse(i, 0, tmp)
                if i % 2 == 1:
                    tmp = tmp[::-1]
                res += tmp[:]

        return res