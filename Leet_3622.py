class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)

        plus = 0
        for i in s :
            plus += int(i)
        
        multi = 1
        for i in s:    
            multi *= int(i)
        
        ans = multi + plus 

        return n % ans == 0 