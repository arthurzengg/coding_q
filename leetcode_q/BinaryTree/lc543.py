# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    # 思路：
    1. 定义一个全局变量 max_dia 用于存储树的最大直径。
    2. 使用深度优先搜索（DFS）遍历整棵树，为每个节点计算其左右子树的最大深度。
    3. 对于每个节点，其可能的最大直径为左子树深度 + 右子树深度。
    4. 在遍历过程中更新全局最大直径 max_dia。
    5. DFS 函数返回当前节点为根的子树的最大深度。
    """

    max_dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_dia

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        left_dia = 0
        right_dia = 0

        if root.left:
            left_dia = left + 1

        if root.right:
            right_dia = right + 1

        self.max_dia = max(self.max_dia, left_dia + right_dia)

        return max(left_dia, right_dia)