class Solution:
    def isHappy(self, n: int) -> bool:
        x = set()
        if n == 1 :
            return True
        while n != 1 and n not in x :
            x.add(n)
            total = 0
            while n > 0 :
                digit = n % 10
                n = n // 10
                total += digit ** 2 
            n = total 
        
        return n == 1
