# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root=ListNode(0)
        root.next=head
        n=root
        while n :
            while n.next and n.next.val==val:
                n.next=n.next.next
            n=n.next
        return root.next