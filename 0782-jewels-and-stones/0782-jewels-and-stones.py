class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=0
        for i in jewels:
            if i in stones:
                s+=stones.count(i)
        return s
        