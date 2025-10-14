class Solution:
    
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans=-float('inf')
        n=len(energy)
        for i in range(n-k,n):
            tot=0
            j=i
            while j>=0:
                tot+=energy[j]
                j-=k
                ans=max(ans,tot)
        return ans
        