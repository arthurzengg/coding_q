# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self. right = right

class Solution:
    def solve(self, p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        if p.left and q.left:
            solve(p.left, q.left)
        if p.right and q.right:
            solve(p.right, q.right)
        return True


sol = Solution()
# print(sol.solve([1]))
