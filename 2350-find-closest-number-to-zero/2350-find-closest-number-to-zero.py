class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        cl=nums[0]
        for i in nums:
            if abs(i)<abs(cl):
                cl=i
        if cl<0 and abs(cl) in nums:
            return abs(cl)
        else:
            return cl

            
            
        