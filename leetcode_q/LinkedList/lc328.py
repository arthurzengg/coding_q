# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    可以大体分为两种情况
    1.odd的后面跟着None
    2.even的后面跟着None
    如果是odd的后面跟着None，比如[1,2,3]，我们需要把None转到even的最后面，因为这odd的后面跟着None代表着一定有even，但是因为even是一定跟在odd后面，所以要把None转到even的最后面
    如果even的后面跟着None，按照while的逻辑，even后面的None是不会动的

    加入even_head = even的逻辑一直有一个指针指向even的开头，遍历完后，odd最后指向even开头就可以了
    """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
