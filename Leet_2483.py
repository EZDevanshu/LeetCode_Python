class Solution:
    def bestClosingTime(self, c: str) -> int:
        yCount = 0
        nCount = 0

        for i in c :
            if i == 'Y' :
                yCount += 1
            
        if yCount == 0 :
            return 0

        li = []

        for i in range(len(c)) :
            li.append(yCount + nCount)
            if c[i] == 'Y' :
                yCount -= 1 
            if c[i] == 'N' :
                nCount += 1
        
        li.append(yCount + nCount)

        mini = li[0]
        idx = 0

        for i in range(len(li)) :
            if  li[i] < mini :
                mini = li[i]
                idx = i
        
        return idx