# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res_list = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            dis = abs(node.val - target)
            res_list.append([dis, node.val])
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res_list.sort()
        return res_list[0][1]


# 或者利用二叉搜索树的特点 更高效率

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val  # 初始化最近值为根节点的值

        def search(node):
            if not node:
                return
            if abs(node.val - target) < abs(self.closest - target):  # 如果当前节点更接近目标值
                self.closest = node.val  # 更新最近值

            # 根据目标值与当前节点值的比较决定搜索方向
            if target < node.val:
                search(node.left)  # 在左子树中搜索
            elif target > node.val:
                search(node.right)  # 在右子树中搜索

        search(root)  # 从根节点开始搜索
        return self.closest
