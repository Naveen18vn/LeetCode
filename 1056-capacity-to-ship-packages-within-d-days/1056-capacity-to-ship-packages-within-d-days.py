class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            dayc=1
            cl=0
            for w in weights:
                if cl +w>cap:
                    dayc+=1
                    cl=0
                cl+=w
            return dayc<=days
        l,r=max(weights),sum(weights)
        while l<r:
            mid=(l+r)//2
            if canShip(mid):
                r=mid
            else:
                l=mid+1
        return l

                
        