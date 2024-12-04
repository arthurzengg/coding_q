# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    此解法用于从给定的二叉树中找到与目标值 target 最接近的 k 个数值。
    思路：
    1. 使用广度优先搜索（BFS）遍历树的每个节点。
    2. 对于每个节点，计算其值与目标值 target 的差的绝对值，并将差值及节点值存入列表。
    3. 将列表按照差值从小到大排序。
    4. 选取排序后列表中的前 k 个元素作为结果返回。

    方法：
    - closestKValues(root, target, k): 主函数，输入根节点、目标值及需要的结果数量，返回最接近的 k 个数值。
    """
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = deque()
        queue.append(root)
        comp_list = []
        res = []

        while queue:
            node = queue.popleft()
            comp_list.append([abs(node.val - target), node.val])
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        comp_list = sorted(comp_list, key=lambda x: x[0])
        for dis, node in comp_list[:k]:
            res.append(node)
        return res
