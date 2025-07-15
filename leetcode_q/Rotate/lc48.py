class Solution:
    """
    解法思路：按照旋转后的映射关系，四个位置成组进行旋转，直接就地交换每一组的 4 个元素。

    具体操作：
    - 对于一个 n x n 的矩阵，旋转过程中每四个元素会构成一个“旋转圈”，即它们之间可以互相交换位置。
    - 比如以下四个点在顺时针旋转后会互换位置：
    (i, j) → (j, n - 1 - i) → (n - 1 - i, n - 1 - j) → (n - 1 - j, i) → 回到 (i, j)
    - 只需要处理矩阵左上角的前半部分（行数为 n // 2，列数为 (n + 1) // 2），就可以完成全部交换。

    为何不需要分奇偶讨论：
    - 当 n 为奇数时，中间行或中间列不动，它们的位置会在四元组旋转中自动处理或保持不变。
    - `(n // 2)` 控制处理的行数，`(n + 1) // 2` 控制列数，可以确保无重复且覆盖所有旋转组。

    时间复杂度：O(n^2)，每个元素处理一次
    空间复杂度：O(1)，原地操作，不使用额外空间
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp

