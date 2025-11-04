class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(m):
            splits=1
            total=0
            for i in nums:
                if total+i>m:
                    splits+=1
                    total=0
                total+=i
            return splits<=k
        l,r=max(nums),sum(nums)
        while l<r:
            m=(l+r)//2
            if split(m):
                r=m
            else:
                l=m+1
        return r
        