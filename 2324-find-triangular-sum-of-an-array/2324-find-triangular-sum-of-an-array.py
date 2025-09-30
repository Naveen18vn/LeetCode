class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        ans=nums
        j=len(nums)
        while j!=1:
            i=0
            while i+1<len(ans):
                ans[i]=(ans[i]+ans[i+1])%10
                i+=1
            j-=1
            ans.pop()
        return ans[0]




        






        