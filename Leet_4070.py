class Solution:
    def minRotations(self, s: str) -> int:
        li = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
        cur = 9
        cost = 0 

        for i in s :
            temp1 = cur
            temp2 = cur
            x = int(i)
            c1 = 0
            c2 = 0
            while(x != li[temp1]) :
                temp1 += 1
                if temp1 == len(li) :
                     temp1 = 9  
                c1 += 1
            
            while(x != li[temp2]) :
                temp2 -= 1
                if temp2 < 9 :
                    temp2 = 18
                c2 += 1
            
            if c1 < c2 :
                cost += c1 
                cur = temp1
            else :
                cost += c2
                cur = temp2

        return cost
             