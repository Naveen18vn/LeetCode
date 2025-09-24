# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n=ListNode(0,head)
        slow=n
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if slow.next.next is not None:
            slow.next=slow.next.next
        else:
            slow.next=None
        return n.next
        