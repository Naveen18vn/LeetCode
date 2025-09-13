class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={}
        c={}
        for i in s:
            if i in ['a','e','i','o','u']:
                if i in v.keys():
                    v[i]+=1
                else:
                    v[i]=1
            else:
                if i in c.keys():
                    c[i]+=1
                else:
                    c[i]=1
        mv=0
        mc=0
        for i,j in v.items():
            if j>=mv:
                mv=j
        for i,j in c.items():
            if j>=mc:
                mc=j
        return mv+mc
        