class Solution:
    """
    此解法用于判断两棵二叉搜索树中是否存在两个节点，它们的值之和等于给定的目标值 target。
    思路：
    1. 使用广度优先搜索（BFS）遍历第一棵树的每个节点。
    2. 对于每个遍历到的节点，计算 complement = target - node.val。
    3. 使用另一个BFS在第二棵树中查找是否存在一个节点的值等于 complement。
    4. 如果在第二棵树中找到这样的节点，则返回 True。
    5. 如果遍历完第一棵树后没有找到符合条件的节点对，则返回 False。

    方法：
    - bfs(value, root): 辅助函数，使用BFS在树中搜索值为 value 的节点。
    - twoSumBSTs(root1, root2, target): 主函数，返回两棵树是否存在两节点值之和为 target 的布尔值。
    """
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def bfs(value, root):
            queue = deque()
            queue.append(root)
            while queue:
                cur_node = queue.popleft()
                if cur_node.val == value:
                    return True
                elif value > cur_node.val and cur_node.right:
                    queue.append(cur_node.right)
                elif value < cur_node.val and cur_node.left:
                    queue.append(cur_node.left)
            return False

        queue = deque()
        queue.append(root1)
        while queue:
            cur_node = queue.popleft()
            if bfs(target - cur_node.val, root2):
                return True
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return False