class Solution:
    """
    此解法用于计算给定二叉树中任意子树的最大平均值。
    思路：
    1. 使用深度优先搜索（DFS）遍历树的每个节点。
    2. 对于每个节点，计算包括该节点在内的所有子节点的值的总和及节点数量。
    3. 根据总和和节点数量计算出每个子树的平均值。
    4. 更新全局最大平均值。
    5. DFS函数返回当前节点的子树的总和和节点数量，以供上层节点计算使用。

    方法：
    - dfs(root): 辅助函数，递归计算每个节点作为根的子树的总和及节点数量，并更新最大平均值。
    - maximumAverageSubtree(root): 主函数，调用dfs并返回最大平均值。
    """

    def __init__(self):
        self.max_average = 0

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def dfs(root):
            if not root:
                return 0, 0
            left_value, left_node_amount = dfs(root.left)
            right_value, right_node_amount = dfs(root.right)

            total_sum = root.val + left_value * left_node_amount + right_value * right_node_amount
            total_amount = left_node_amount + right_node_amount + 1

            average = total_sum / total_amount
            self.max_average = max(self.max_average, average)
            return average, left_node_amount + right_node_amount + 1

        dfs(root)
        return self.max_average