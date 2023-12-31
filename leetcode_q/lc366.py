'''
讲解视频： https://www.youtube.com/watch?app=desktop&v=L0HY4Ha_2Ow
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def post_order(node):
            nonlocal lookup

            if not node:
                return 0
            left_depth = post_order(node.left)
            right_depth = post_order(node.right)
            curr_depth = max(left_depth, right_depth) + 1
            lookup[curr_depth].append(node.val)
            return curr_depth

        lookup = defaultdict(list)
        post_order(root)
        return lookup.values()