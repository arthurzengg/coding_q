# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        elif not left and right:
            return right
        elif left and not right:
            return left
        else:
            return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(nums, index):
    if index >= len(nums):
        return
    if nums[index] == -1:
        return None
    left = index * 2 + 1
    right = index * 2 + 2
    root = TreeNode(nums[index])
    root.left = construct_binary_tree(nums, left)
    root.right = construct_binary_tree(nums, right)
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


nums = [1,2]
root = construct_binary_tree(nums, 0)
p_val = 1
q_val = 2

p_node = find_node(root, p_val)
q_node = find_node(root, q_val)

sol = Solution()
lca = sol.lowestCommonAncestor(root, p_node, q_node)
print(lca.val if lca else None)