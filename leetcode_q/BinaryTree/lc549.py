class Solution:
    """
    # 思路：
    1. 使用深度优先搜索（DFS）遍历树，并对每个节点计算以该节点为中心的最长递增和递减连续序列。
    2. 对于每个节点，通过左右子节点返回的递增（inc）和递减（dec）序列长度，确定当前节点能够延伸的最长序列长度。
    3. 对于树中的每个节点，计算可能的最长连续路径（可以是递增后跟递减，或递减后跟递增）。
    4. 更新全局最大长度 max_len，此长度为遍历过程中遇到的最长的连续路径长度。
    5. DFS 函数返回一个元组 (inc, dec)，其中 inc 为从当前节点开始的最长递增序列长度，dec 为最长递减序列长度。
    """

    max_len = 1  # 初始化全局最长连续序列长度为1，因为至少包含自身

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)  # 从根节点开始深度优先搜索
        return self.max_len  # 返回计算得到的最长连续序列长度

    def dfs(self, root):
        if not root:
            return (0, 0)  # 如果节点为空，返回长度为0

        left = self.dfs(root.left)  # 递归左子树
        right = self.dfs(root.right)  # 递归右子树

        inc = 1  # 初始化以当前节点为起点的递增序列长度
        dec = 1  # 初始化递减序列长度

        if root.left:  # 处理左子节点
            if root.val - root.left.val == 1:
                inc = left[0] + 1  # 如果左子节点值小于当前节点值，递增序列加1
            elif root.val - root.left.val == -1:
                dec = left[1] + 1  # 如果左子节点值大于当前节点值，递减序列加1

        if root.right:  # 处理右子节点
            if root.val - root.right.val == 1:
                inc = max(inc, right[0] + 1)  # 选择最长的递增序列
            elif root.val - root.right.val == -1:
                dec = max(dec, right[1] + 1)  # 选择最长的递减序列

        self.max_len = max(self.max_len, inc + dec - 1)  # 更新全局最长序列长度

        return (inc, dec)  # 返回当前节点的递增和递减序列长度