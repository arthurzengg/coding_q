class Solution:
    """
    具体实现方法如下：
    1. 将二维矩阵看作是一个排序的一维数组，进行二分查找。数组的长度为 n*m，其中 n 是矩阵的行数，m 是矩阵的列数。
    2. 计算中间元素的位置 mid，通过 mid 可以计算出对应的行号 row = mid // m 和列号 col = mid % m。
    3. 比较矩阵中的元素 matrix[row][col] 和目标值 target：
       - 如果 matrix[row][col] 等于 target，返回 True。
       - 如果 matrix[row][col] 大于 target，更新搜索范围的右界 right = mid - 1。
       - 如果 matrix[row][col] 小于 target，更新搜索范围的左界 left = mid + 1。
    4. 如果在整个矩阵中没有找到 target，则返回 False。

    关键点：
    - 利用矩阵的行有序和列有序的特点，可以将矩阵视为一个有序的一维数组来应用二分查找。
    - 使用整除和取模操作方便地从一维索引映射到二维位置。
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = row * m + col - 1
            else:
                left = row * m + col + 1
        return False