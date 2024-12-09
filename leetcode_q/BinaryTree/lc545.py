# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    此解法用于找到二叉树的边界节点，包括左边界、叶子节点、和右边界（逆序）。
    思路：
    1. 分别定义函数处理左边界、叶子节点和右边界的查找。
    2. 先添加根节点到结果中，然后依次处理左边界（不包括最底部的叶子节点）、所有的叶子节点（从左到右），最后处理右边界（需要逆序添加，且不包括最底部的叶子节点）。
    3. 左边界的定义：从根节点的左子节点开始，优先取左子节点，没有左子节点则取右子节点，一直到达叶子节点前的最后一个节点。
    4. 右边界的定义：从根节点的右子节点开始，优先取右子节点，没有右子节点则取左子节点，一直到达叶子节点前的最后一个节点。
    5. 叶子节点的定义：不具有任何子节点的节点。

    方法：
    - boundaryOfBinaryTree(root): 主函数，整合所有边界节点并返回。
    - find_left_boundary(root, depth): 递归寻找左边界节点。
    - find_leaves(root): 递归寻找叶子节点。
    - find_right_boundary(root, depth): 递归寻找右边界节点。
    """

    def __init__(self):
        self.left_boundary = []
        self.right_boundary = []
        self.leaves = []

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        self.find_left_boundary(root.left, 1)
        if self.left_boundary:
            for i in range(len(self.left_boundary) - 1):
                res.append(self.left_boundary[i])
        self.find_leaves(root.left)
        self.find_leaves(root.right)
        if self.leaves:
            for node in self.leaves:
                res.append(node)
        self.find_right_boundary(root.right, 1)
        if self.right_boundary:
            for i in range(1, len(self.right_boundary[::-1])):
                res.append(self.right_boundary[::-1][i])
        return res

    def find_left_boundary(self, root, depth):
        if not root:
            return
        if depth > 0:
            self.left_boundary.append(root.val)
        if root.left:
            self.find_left_boundary(root.left, depth + 1)
        elif root.right:
            self.find_left_boundary(root.right, depth + 1)

    def find_leaves(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.leaves.append(root.val)
        if root.left:
            self.find_leaves(root.left)
        if root.right:
            self.find_leaves(root.right)

    def find_right_boundary(self, root, depth):
        if not root:
            return
        if depth > 0:
            self.right_boundary.append(root.val)
        if root.right:
            self.find_right_boundary(root.right, depth + 1)
        elif root.left:
            self.find_right_boundary(root.left, depth + 1)

