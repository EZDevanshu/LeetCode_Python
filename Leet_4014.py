class Solution:
    def minPrice(self, p: list[int], d: list[int]) -> float:
        totalPrice = 0
        p.sort()
        d.sort()
        i = len(p) - 1
        j = len(d) - 1
        
        while j >= 0 and i >= 0:
            totalPrice += p[i] * (100 - d[j]) / 100
            j-=1
            i-=1

        while i >= 0 :
            totalPrice += p[i]
            i-=1

        return totalPrice