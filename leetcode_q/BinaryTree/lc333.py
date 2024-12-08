# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    此解法用于寻找给定二叉树中最大的二叉搜索子树（BST）的节点数量。
    思路：
    1. 使用深度优先搜索（DFS）遍历树的每个节点。
    2. 对于每个节点，返回四个信息：子树的大小、子树中的最小值、子树中的最大值、子树是否为BST。
    3. 如果一个节点的左右子树都是BST，并且该节点的值大于左子树的最大值且小于右子树的最小值，则该节点及其子树形成一个更大的BST。
    4. 在每个有效的BST节点处，更新记录的最大BST大小。
    5. 如果当前节点的子树不满足BST的条件，返回False，并阻止父节点成为BST的一部分。

    方法：
    - dfs(root): 递归函数，遍历树节点，计算BST的属性并更新最大BST大小。
    - largestBSTSubtree(root): 主函数，初始化全局变量，调用dfs函数，并返回最大BST的大小。
    """

    def __init__(self):
        self.largestBST = 1

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0, float('inf'), float('-inf'), True

            left_size, left_min, left_max, left_is_bst = dfs(root.left)
            right_size, right_min, right_max, right_is_bst = dfs(root.right)

            if left_is_bst and right_is_bst and left_max < root.val < right_min:
                self.largestBST = max(self.largestBST, left_size + right_size + 1)
                return left_size + right_size + 1, min(left_min, root.val), max(right_max, root.val), True
            else:
                return 0, 0, 0, False

        dfs(root)
        return self.largestBST
