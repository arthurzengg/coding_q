# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    此解法用于统计一棵二叉树中的单值子树数量。
    思路：
    1. 使用深度优先搜索（DFS）遍历每个节点。
    2. 对于每个节点，检查其所有子节点的值是否与当前节点相同。
    3. 如果一个节点的左右子树都是单值子树，并且它们的值与当前节点的值相同（或者是叶子节点），则当前节点也是单值子树。
    4. 通过递归的方式，从叶子节点向上返回每个节点是否是单值子树，并累计单值子树的数量。

    方法：
    - dfs(root): 递归函数，用于判断以root为根的子树是否是单值子树，并返回其状态和值。
    - countUnivalSubtrees(root): 主函数，初始化全局计数器，调用dfs函数，并返回单值子树的数量。
    """

    def __init__(self):
        self.res = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return True, -1
            left, left_value = dfs(root.left)
            right, right_value = dfs(root.right)

            if left and right:
                if left_value == right_value == -1:
                    self.res += 1
                    return True, root.val
                elif left_value == right_value == root.val:
                    self.res += 1
                    return True, root.val
                elif left_value == -1 and right_value == root.val:
                    self.res += 1
                    return True, root.val
                elif right_value == -1 and left_value == root.val:
                    self.res += 1
                    return True, root.val
            return False, root.val

        dfs(root)

        return self.res

