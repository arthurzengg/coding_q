# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    此解法用于将单链表中的所有负数节点移动到非负数节点之前。
    思路：
    1. 创建一个虚拟头节点 dummy，其 next 指向原链表的头节点 head，方便处理在头部插入节点的情况。
    2. 使用两个指针 pre 和 cur 遍历链表。pre 始终指向 cur 指针的前一个节点，这样便于重新链接节点。
    3. 当 cur 指向的节点的值为负数时，将该节点移动到链表的最前面，并更新 head 指向新的头节点。
    4. 如果 cur 指向的节点的值不是负数，只需要简单地继续向后移动 pre 和 cur 指针。
    5. 最后返回 dummy.next 作为新链表的头部。

    方法：
    - sortLinkedList(head): 输入链表的头节点，返回排序后的链表头节点。
    """

    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        pre = head
        cur = head.next

        while cur:
            next_node = cur.next
            if cur.val < 0:
                dummy.next = cur
                cur.next = head
                pre.next = next_node
                cur = next_node
                head = dummy.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next

