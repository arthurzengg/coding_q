# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    # 思路：
    给定一个链表，按照每 k 个节点一组来进行翻转。如果节点总数不是 k 的整数倍，最后剩余节点保持原有顺序。
    - 使用一个哑节点(dummy node)作为新链表的头部，便于处理链表头部的翻转情况。
    - 使用三个指针 pre、cur 和 end，其中 pre 指向当前要翻转的 k 个节点的前一个节点，cur 指向当前要翻转的第一个节点，end 指向当前要翻转的最后一个节点。
    - 通过循环移动 end 指针来确认是否有足够的节点进行翻转。如果不足 k 个，结束循环。
    - 断开当前要翻转的部分和剩余部分的连接，然后进行翻转，并重新连接翻转后的部分和之前的部分。

    方法：
    - reverseKGroup：主函数，控制翻转的整体逻辑。
    - reverse：辅助函数，用于翻转链表的一部分，并返回新的头部和尾部。
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        end = head

        while end:
            for _ in range(k - 1):
                if end:
                    end = end.next
            if not end:
                break
            temp = end.next
            end.next = None
            reverseNode, last_point = self.reverse(cur)
            pre.next = reverseNode
            last_point.next = temp

            cur = temp
            pre = last_point
            end = temp
        return dummy.next

    def reverse(self, head):
        cur = head
        pre = None
        count = 0
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            if count == 0:
                last_point = pre
                count += 1
            cur = temp
        return pre, last_point
