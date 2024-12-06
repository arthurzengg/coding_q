class Solution:
    """
    此解法用于验证给定的数组是否为某二叉搜索树的前序遍历结果。
    思路：
    1. 使用一个栈来维持遍历的历史节点，以便于回溯并调整最小可能的节点值。
    2. 设定一个最小节点值 min_node，用于记录当前节点值必须超过的最小值，初始为负无穷。
    3. 遍历前序遍历的数组，对于每个节点值：
       - 如果该节点值小于 min_node，则直接返回 False，因为它违反了二叉搜索树的性质。
       - 否则，当当前节点值大于栈顶元素时，弹出栈顶元素并更新 min_node，表示我们已经完成了该子树的遍历。
       - 将当前节点值压入栈中。
    4. 如果整个数组遍历完毕都没有发现问题，则返回 True，表示该数组可以是某BST的前序遍历结果。

    方法：
    - verifyPreorder(preorder): 输入前序遍历数组，返回是否有效的布尔值。
    """

    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_node = float('-inf')
        stack = []
        for node in preorder:
            if node < min_node:
                return False
            while stack and node > stack[-1]:
                min_node = stack.pop()
            stack.append(node)
        return True
