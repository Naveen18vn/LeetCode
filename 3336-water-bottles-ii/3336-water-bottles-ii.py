class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        BottlesD=numBottles
        eb=numBottles
        while eb>=numExchange:
            eb-=numExchange
            numExchange+=1
            eb+=1
            BottlesD+=1
        return BottlesD


        