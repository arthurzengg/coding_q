class Solution:
    """
    本解决方案使用中序遍历来验证二叉搜索树（BST）的有效性。
    中序遍历按照左-根-右的顺序访问树的所有节点，并应当按照递增顺序访问所有节点的值，
    如果不是递增顺序，则不是有效的BST。

    Attributes:
        prev (TreeNode): 指向在中序遍历过程中最后访问的节点。
    """

    prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, root):
        if not root:
            return True

        left = self.inorder(root.left)

        if not left:
            return False

        if self.prev and root.val <= self.prev.val:
            return False

        self.prev = root

        return self.inorder(root.right)
