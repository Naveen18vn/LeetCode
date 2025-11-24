class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dp=[0]*1001
        for num,start,end in trips:
            dp[start]+=num
            dp[end]-=num
        cur=0
        for i in dp:
            cur+=i
            if cur>capacity:
                return False
        return True


            

        