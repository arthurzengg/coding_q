class Solution:
    """
    # 思路：
    使用归并排序算法对链表进行排序。归并排序适合链表这种数据结构，因为它可以在O(1)的空间复杂度下进行，
    不需要像数组那样频繁地进行位置交换。

    方法：
    - 分割链表：递归地将链表分割成两半，直到每个子链表只有一个节点或为空。
    - 寻找中点：使用快慢指针技巧找到链表的中点，快指针每次移动两步，慢指针每次移动一步。
    - 合并链表：将两个排序好的子链表合并成一个有序的链表。
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # 找到中点，并分割链表
        mid = self.midListNode(head)
        right = mid.next
        mid.next = None
        left = head
        
        # 递归排序左右两部分
        return self.merge(self.sortList(left), self.sortList(right))

    def midListNode(self, head):
        """
        使用快慢指针找到链表的中点。
        """
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        """
        合并两个已排序的链表。
        """
        res = ListNode()
        temp = res
        while left and right:
            if left.val <= right.val:
                temp.next = ListNode(left.val)
                left = left.next
            else:
                temp.next = ListNode(right.val)
                right = right.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return res.next