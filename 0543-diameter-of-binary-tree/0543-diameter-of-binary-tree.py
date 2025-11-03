# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        l=[0]
        def height(root):
            if not root:
                return 0
            left_h=height(root.left)
            right_h=height(root.right)
            d=left_h+right_h
            l[0]=max(l[0],d)
            return 1+max(left_h,right_h)
        height(root)
        return l[0]

        