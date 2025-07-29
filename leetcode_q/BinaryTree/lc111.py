# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    使用 DFS 遍历所有路径，记录每条从根到叶子的深度，取最小值。
    注意 Python 中闭包对外部变量的修改需用 nonlocal，否则无法更新结果。
    """

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float('inf')

        def dfs(root, depth):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res = min(res, depth)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return res