class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0 :
            return 0
        num = str(n)

        li = [int(i) for i in num]

        total = 0
        x = ""
        for i in li:
            if i != 0 :
                total += i
                x += str(i)
        
        y = int(x)
        return total * y