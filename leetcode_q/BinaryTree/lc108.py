# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    # 思路：
    将一个按非递减顺序排序的整数数组转换为一棵高度平衡的二叉搜索树（BST）。
    高度平衡的二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。

    方法：
    - 递归地将数组的中间元素作为树的根节点，中间元素左侧的数组构造左子树，右侧数组构造右子树。
    - 当数组只有一个元素时，直接返回该元素作为树的节点。
    - 当数组有两个元素时，选择第二个元素作为根节点，第一个元素作为根节点的左子节点。
    - 对数组进行分割，并对每一部分递归执行相同的操作。
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums.sort()

        def bst(nums):
            n = len(nums)
            if n == 1:
                return TreeNode(nums[0])
            if n == 2:
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                return root
            mid = n // 2
            root = TreeNode(nums[mid])
            root.left = bst(nums[:mid])
            root.right = bst(nums[mid + 1:])
            return root

        return bst(nums)
