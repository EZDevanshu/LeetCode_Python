class Solution:
    def maxProduct(self, n: int) -> int:
        num = str(n)
        li = []
        for i in num :
            li.append(int(i))

        li.sort()
    
        return li[-1] * li[-2]