class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp = n 
        while True : 
            mul = 1
            convert_into_str = str(temp)
            for i in convert_into_str :
                mul *= int(i)
            
            if mul % t == 0:
                return temp
            temp+= 1
       