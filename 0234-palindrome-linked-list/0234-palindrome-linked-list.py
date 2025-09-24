# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        temp=head
        if temp==None:
            return True            
        while temp:
            l.append(temp.val)
            temp=temp.next
        l2=l[::-1]
        return l==l2
        