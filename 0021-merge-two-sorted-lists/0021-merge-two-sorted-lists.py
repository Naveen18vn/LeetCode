# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root=n=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                val=list1.val
                list1=list1.next
                n.next=ListNode(val)
                n=n.next
            elif list2.val<list1.val:
                val=list2.val
                list2=list2.next
                n.next=ListNode(val)
                n=n.next
            else:
                val=list1.val
                list1=list1.next
                list2=list2.next
                n.next=ListNode(val)
                n=n.next
                n.next=ListNode(val)
                n=n.next
        if list1:
            while list1:
                val=list1.val
                list1=list1.next
                n.next=ListNode(val)
                n=n.next
        if list2:
            while list2:
                val=list2.val
                list2=list2.next
                n.next=ListNode(val)
                n=n.next
        return root.next

