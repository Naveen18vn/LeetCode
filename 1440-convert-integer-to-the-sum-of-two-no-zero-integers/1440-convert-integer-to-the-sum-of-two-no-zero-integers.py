class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def c(x):
            return '0' not in str(x)
        for i in range(1,n):
            j=n-i
            if c(i) and c(j):
                return [i,j]

