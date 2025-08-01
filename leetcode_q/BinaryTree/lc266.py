class Solution:
    """
    思路解析：
    - 本题要求我们将一棵二叉树进行“翻转”，也就是将每一个节点的左右子树互换。
    - 这类题目天然适合使用递归（DFS 深度优先搜索）来解决。

    解法步骤：
    1. 从根节点开始进行递归。
    2. 对于每一个节点，先递归地翻转它的右子树，再递归地翻转它的左子树。
    3. 然后将左右子树交换。
    4. 递归终止条件是当前节点为 None，直接返回 None。

    时间复杂度：O(n)，其中 n 为树中节点个数，每个节点访问一次。
    空间复杂度：O(h)，递归栈的最大深度为树的高度，最坏为 O(n)，最优为 O(log n)。
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            root.left, root.right = dfs(root.right), dfs(root.left)
            return root

        root = dfs(root)
        return root