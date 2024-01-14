from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # 如果根节点为空，返回空列表

        col_table = defaultdict(list)  # 使用字典来存储每一列的节点值
        queue = [(root, 0)]  # 初始化队列，包括节点和其对应的列索引
        res = []  # 初始化结果列表

        while queue:  # 当队列不为空时
            for _ in range(len(queue)):  # 遍历当前队列中的所有节点（当前层）
                node, col = queue.pop(0)  # 从队列中取出节点和列索引
                col_table[col].append(node.val)  # 将节点值添加到对应列的列表中

                # 如果存在左子节点，将其及其列索引（当前列索引减1）加入队列
                if node.left:
                    queue.append((node.left, col - 1))

                # 如果存在右子节点，将其及其列索引（当前列索引加1）加入队列
                if node.right:
                    queue.append((node.right, col + 1))

        # 将列索引排序，以确保从左到右的顺序
        sorted_order = list(col_table.keys())
        sorted_order.sort()

        # 按照排序后的列索引顺序，将节点值添加到结果列表
        for index in sorted_order:
            res.append(col_table[index])

        return res  # 返回结果列表
