class Solution:
    """
    目标是在矩阵中查找某个 target 是否存在，返回 True 或 False。
    思路如下：
    1. 观察矩阵性质可知，整张矩阵可以视为一个“升序的一维数组”，但我们采用逐行策略处理。
    2. 首先遍历每一行的最后一个元素：
    - 如果该值等于 target，直接返回 True；
    - 如果该值大于 target，说明 target 有可能在这一行，于是将该行加入候选行。
    3. 对所有候选行使用二分查找：
    - 对每一行从左到右进行标准的二分查找；
    - 如果找到 target，返回 True。
    4. 如果所有候选行中都没找到目标值，则返回 False。
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] > target:
                target_row.append(i)

        for i in target_row:
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    right = mid
                else:
                    left = mid + 1
        return False
