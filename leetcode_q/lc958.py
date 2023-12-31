# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, currNodes, totalNodes):
            if not node:
                return True
            if currNodes > totalNodes:
                return False
            return dfs(node.left, currNodes * 2, totalNodes) and dfs(node.right, currNodes * 2 + 1, totalNodes)

        def countNodes(node):
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)
        print(countNodes(root))

        return dfs(root, 1, countNodes(root))