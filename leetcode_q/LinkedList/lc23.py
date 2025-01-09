class Solution:
    """
    # 思路：
    使用分治法将合并 k 个排序链表的问题分解成合并两个链表的问题。
    分治法的基本思想是将原问题分解成若干个规模较小的问题，递归解决这些小问题，
    然后将所有的解合并成原问题的解。

    方法：
    - 递归地将链表列表分成两半，直到每个子问题只包含一个链表。
    - 使用合并两个链表的方法，递归地合并每对链表，最终得到合并后的链表。

    功能：
    - mergeKLists：接受一个链表数组，返回合并后的链表。
    - findMid：递归分治方法，用于找到中点并递归地合并链表。
    - mergeList：合并两个链表。
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        return self.findMid(lists, 0, n - 1)

    def findMid(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        left = self.findMid(lists, left, mid)
        right = self.findMid(lists, mid + 1, right)
        return self.mergeList(left, right)

    def mergeList(self, left, right):
        res = ListNode()
        temp = res
        while left and right:
            if left.val < right.val:
                temp.next = ListNode(left.val)
                temp = temp.next
                left = left.next
            else:
                temp.next = ListNode(right.val)
                temp = temp.next
                right = right.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return res.next