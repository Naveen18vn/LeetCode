class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        mini=float('inf')
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                s-=nums[l]
                mini=min(mini,r-l+1)
                l+=1
        return mini if mini <float('inf') else 0
