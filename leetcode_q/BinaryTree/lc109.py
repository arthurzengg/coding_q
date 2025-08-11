# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    中文思路解析：
    目标：将有序链表转换为高度平衡的二叉搜索树（BST）。

    思路（数组中点建树）：
    1) 先把链表整体扫一遍，存到数组 temp 中。链表是升序，temp 也升序。
    2) 用分治递归：对任意区间 [start, end]，选择中点 mid 作为根节点，
       左半段构建左子树，右半段构建右子树。这样天然让树左右高度尽量接近，满足平衡要求。
    3) 递归终止：start > end 返回 None。

    正确性：BST 中序序列为升序；本方法等价于“从有序数组构建平衡 BST”的标准做法，
    中点为根保证左右子树节点数量尽量接近，从而近似平衡。

    复杂度：
    - 时间：O(n)，遍历链表 O(n) + 构建树每个元素用一次 O(n)。
    - 空间：O(n)，需要数组存储链表值；递归栈平均 O(log n)，最坏 O(n)。

    备注：
    - 若需将额外空间从 O(n) 降为 O(1)，可用快慢指针每次找链表中点，或用“模拟中序构建”的方法，
      但实现更复杂、常数大。当前解法更直观，也足以通过。
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        pre = head
        temp = []
        while pre:
            temp.append(pre.val)
            pre = pre.next

        def construct_tree(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            root = TreeNode(temp[mid])
            root.left = construct_tree(start, mid - 1)
            root.right = construct_tree(mid + 1, end)
            return root

        root = construct_tree(0, len(temp) - 1)
        return root
