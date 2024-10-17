# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next:
            for i in range(m):
                if not cur.next: # 如果没有更多节点，则退出
                    return dummy.next
                cur = cur.next

            temp = cur.next
            for j in range(n):
                if not temp:  # 如果没有更多节点可供删除，直接退出
                    break
                temp = temp.next
            cur.next = temp
        return dummy.next