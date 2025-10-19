# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l=[]
        temp=head
        while temp!=None:
            l.append(temp.val)
            temp=temp.next
        l=l[::-1]
        res=0
        for i in range(len(l)):
            res+=l[i]*(2**i)
        return res

