class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        s=""
        res=[]
        for i in range(len(nums)):
            a=s+str(nums[i])
            s=a
            res.append(int(s,2)%5==0) 
        return res

            
            

       