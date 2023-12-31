# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 对于一颗搜索树，从root.val开始搜索，它父节点的左节点的下限是-无穷，父节点的右节点的上限是+无穷
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            # 当搜索到叶节点就返回True
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            # 下一个dfs的父节点（也就是当前父节点的左节点）的下限依然是负无穷，但上限是当前父节点值（node.val)
            if not dfs(node.left, lower, node.val):
                return False
            # 同理
            if not dfs(node.right, node.val, upper):
                return False
            return True
        return dfs(root)