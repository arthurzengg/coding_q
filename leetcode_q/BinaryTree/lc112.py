# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    解法思路：使用 DFS（递归）遍历整棵树，并在递归过程中逐步减去路径上的节点值，判断是否存在满足条件的路径。

    具体步骤：
    1. 若当前节点为空，说明路径不存在，返回 False；
    2. 若当前节点是叶子节点（没有左子树和右子树），则判断当前节点值是否等于 targetSum；
    - 如果相等，说明存在一条合法路径，返回 True；
    - 否则返回 False；
    3. 否则递归遍历左右子树，并更新目标值为 targetSum - 当前节点值；
    - 如果任意一边返回 True，说明存在合法路径。

    时间复杂度：O(n)，其中 n 为节点总数，每个节点最多访问一次；
    空间复杂度：O(h)，递归栈深度，h 为树的高度。
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            if not root:
                return False
            if not root.left and not root.right:
                return root.val == targetSum

            left = dfs(root.left, targetSum - root.val)
            right = dfs(root.right, targetSum - root.val)
            return left or right

        if dfs(root, targetSum):
            return True
        else:
            return False