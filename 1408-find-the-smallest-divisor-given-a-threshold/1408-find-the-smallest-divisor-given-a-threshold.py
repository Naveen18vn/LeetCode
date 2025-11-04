class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def thrsh(k):
            s=0
            for i in nums:
                s+=ceil(i/k)
            return s<=threshold   
        l,r=1,max(nums)
        while l<r:
            m=(l+r)//2
            if thrsh(m):
                r=m
            else:
                l=m+1
        return l