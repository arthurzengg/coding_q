"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    """
    此解法用于克隆一个无向图。图由节点组成，每个节点包含一个值和一个邻居节点列表。
    思路：
    1. 如果输入的节点为空，则返回 None。
    2. 使用一个字典 seen 来记录所有已经访问并克隆过的节点，键是原节点的值，值是克隆的新节点。
    3. 定义一个深度优先搜索函数 dfs，用于遍历图并克隆节点：
       - 对于每个遍历到的节点，如果它已经在 seen 中有对应的克隆节点，则直接返回该克隆节点。
       - 如果还没有克隆过，创建一个新的节点，并将其添加到 seen 中。
       - 遍历当前节点的所有邻居，对每个邻居递归调用 dfs 函数，并将返回的克隆节点添加到当前克隆节点的邻居列表中。
    4. 从给定的起始节点开始调用 dfs 函数，返回克隆的图的根节点。
    """

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}

        def dfs(node):
            copy = Node(node.val)
            seen[node.val] = copy
            for i in node.neighbors:
                if i.val in seen:
                    copy.neighbors.append(seen[i.val])
                else:
                    copy.neighbors.append(dfs(i))
            return copy

        return dfs(node)
