# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        d=ListNode()
        d.next=head
        a=d
        b=d
        for _ in range(n+1):
            a=a.next
        while a:
            a=a.next
            b=b.next
        b.next=b.next.next
        return d.next
        

        