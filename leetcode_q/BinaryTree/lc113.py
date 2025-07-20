# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    使用 BFS（广度优先搜索）方式遍历树：
    1. 队列中保存三元组：(当前节点，当前路径列表，剩余目标值)；
    2. 每次出队时将当前节点值加入路径；
    3. 如果当前节点是叶子节点，并且剩余值刚好等于节点值，则找到一条合法路径；
    4. 否则，将左右子节点连同新的路径和更新的 targetSum 加入队列。

    ⚠️ 注意：路径 `path` 是列表，必须拷贝（`path + [node.val]`），否则左右子树会共享同一个 path，导致结果错误。

    时间复杂度：O(n²)，路径拷贝开销
    空间复杂度：O(n)
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        queue = [(root, [], targetSum)]
        while queue:
            node, path, target = queue.pop(0)
            if not node:
                continue
            tmp_path = path + [node.val]
            if not node.left and not node.right:
                if node.val == target:
                    res.append(tmp_path)
            queue.append((node.left, tmp_path, target - node.val))
            queue.append((node.right, tmp_path, target - node.val))
        return res
