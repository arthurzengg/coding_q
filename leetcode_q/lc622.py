class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0  # 用于存储最大宽度
        queue = [(1, root)]  # 初始化队列，存储节点及其在树中的位置索引

        while queue:  # 当队列不为空时
            most_left = float('inf')  # 当前层最左节点的索引
            most_right = 0  # 当前层最右节点的索引
            for _ in range(len(queue)):  # 遍历当前层的所有节点
                index, node = queue.pop(0)  # 弹出队列首部元素，得到节点及其索引

                # 将左子节点加入队列（如果存在）
                if node.left:
                    queue.append((index * 2, node.left))
                # 将右子节点加入队列（如果存在）
                if node.right:
                    queue.append((index * 2 + 1, node.right))

                # 更新当前层的最左和最右索引
                most_left = min(most_left, index)
                most_right = max(most_right, index)

            # 更新全局最大宽度
            ans = max(ans, most_right - most_left + 1)

        return ans  # 返回最大宽度
