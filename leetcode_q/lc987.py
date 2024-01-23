# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = defaultdict(list)
        queue = [[root, 0, 0]]
        res = []
        while queue:
            node, row, col = queue.pop(0)
            node_list[col].append([row, node.val])
            if node.left:
                queue.append([node.left, row + 1, col - 1])
            if node.right:
                queue.append([node.right, row + 1, col + 1])
        sorted_cols = sorted(node_list.keys())
        for col in sorted_cols:
            res.append([val for row, val in sorted(node_list[col])])
        return res

