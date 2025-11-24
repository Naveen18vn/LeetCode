class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nextG={}
        for i in nums2:
            while stack and stack[-1]<i:
                nextG[stack.pop()]=i
            stack.append(i)
        for i in stack:
            nextG[i]=-1
        return [nextG[n] for n in nums1]
            
        