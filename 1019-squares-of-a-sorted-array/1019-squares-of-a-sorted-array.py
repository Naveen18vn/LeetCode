class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        j=n-1
        ans=[]
        while i <=j:
            if abs(nums[i])>abs(nums[j]):
                ans.append(nums[i]*nums[i])
                i+=1
            else:
                ans.append(nums[j]*nums[j])
                j-=1
        ans=ans[::-1]
        return ans