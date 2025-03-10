# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    中文思路解析：
    本题要求在二叉搜索树（BST）中删除一个指定值的节点，并保证删除后仍然是BST。
    删除节点的情况分为以下几种：

    1. 如果目标节点是叶子节点（无子节点），直接删除（返回 None）。
    2. 如果目标节点只有一个子节点（左或右），用这个子节点替换目标节点。
    3. 如果目标节点同时有左右子节点：
       - 找到右子树中的最小节点（即右子树中最左侧的节点），称为后继节点（successor）。
       - 将目标节点的值替换为后继节点的值。
       - 然后在右子树中递归删除这个继任节点。

    关键辅助函数：
    - find_min(node)：用于找到右子树中值最小的节点，即 successor（后继节点）。

    算法实现细节：
    - 因为是在二叉搜索树中删除节点，利用BST的特性进行搜索，保证了算法的高效性。
    - 每次删除节点之后都要保证树的结构仍然符合BST定义。
    """

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 在左子树中搜索待删除节点
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # 在右子树中搜索待删除节点
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # 找到目标节点
        else:
            # 情况1：叶子节点，直接删除
            if not root.left and not root.right:
                return None

            # 情况2：只有一个子节点
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left

            # 情况3：节点同时拥有左右子节点
            successor = self.find_min(root.right)  # 找右子树的最小节点
            root.val = successor.val  # 用 successor 替换当前节点的值
            root.right = self.deleteNode(root.right, successor.val)  # 删除 successor 节点

        return root

    def find_min(self, node):
        """
        在BST中寻找以node为根的子树中的最小值节点，即最左边的节点。
        """
        while node.left:
            node = node.left
        return node