class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def can_a(k):
            total=0
            for i in dist[:-1]:
                total+=ceil(i/k)
            total+=dist[-1]/k
            return total<=hour
        if hour<=len(dist)-1:
            return -1
        l=1
        r=10**7
        while l<r:
            mid=(l+r)//2
            if can_a(mid):
                r=mid
            else:
                l=mid+1
        return r

      