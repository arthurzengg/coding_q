# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    此解法用于对单链表表示的非负整数进行加一操作。
    思路：
    1. 使用一个虚拟头节点 dummy 指向原链表头，以便处理头节点进位的情况。
    2. 使用一个指针 not_nine 遍历链表，记录最后一个不是9的节点。
    3. 再次遍历链表，从头节点到最后一个不是9的节点（not_nine），其后的节点如果是9则需要置0。
    4. 对最后一个不是9的节点加一。
    5. 如果加一操作导致 dummy 节点的值变为1，说明有进位从头部产生，此时直接返回 dummy 节点。
    6. 否则返回原链表头节点。

    方法：
    - plusOne(head): 输入链表的头节点，返回加一后的链表头节点。
    """

    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        not_nine = dummy

        cur = head
        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next

        not_nine.val += 1

        cur = not_nine.next
        while cur:
            cur.val = 0
            cur = cur.next
        if dummy.val == 1:
            return dummy
        return head
