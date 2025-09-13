class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1=abs(z-x)
        p2=abs(z-y)
        if p1<p2:
            return 1
        elif p2<p1:
            return 2
        else:
            return 0


        