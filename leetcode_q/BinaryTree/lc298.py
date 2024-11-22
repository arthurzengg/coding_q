# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    # 思路：
    1. 使用广度优先搜索（BFS）遍历二叉树的每个节点。
    2. 对每个节点，记录从根到该节点的连续序列。
    3. 如果子节点的值是当前节点的值加一，则将子节点的值加入到当前序列中。
    4. 否则，从子节点开始一个新的序列。
    5. 使用队列来维持待处理的节点和其对应的连续序列。
    6. 记录并更新遇到的最长连续序列的长度。
    """

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 1

        queue = deque()
        queue.append([root, [root.val]])

        while queue:
            node, consecutive_list = queue.popleft()
            if node.left:
                left_list = consecutive_list[:]
                if node.left.val == node.val + 1:
                    left_list.append(node.left.val)
                    queue.append([node.left, left_list])
                else:
                    queue.append([node.left, [node.left.val]])
                max_len = max(max_len, len(left_list))
            if node.right:
                right_list = consecutive_list[:]
                if node.right.val == node.val + 1:
                    right_list.append(node.right.val)
                    queue.append([node.right, right_list])
                else:
                    queue.append([node.right, [node.right.val]])
                max_len = max(max_len, len(right_list))
        return max_len