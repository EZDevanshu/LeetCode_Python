class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        li = []
        
        for i in timePoints :
            hours , minute = map(int , i.split(":"))

            if (hours == 0) and (minute == 0) :
                totalTime = 1440
            else :
                totalTime = (hours * 60) + minute

            li.append(totalTime)
        
        li.sort()

        mindiff = float('inf')

        for i in range(1, len(li)) :
            mindiff = min(mindiff , li[i] - li[i - 1])

        mindiff = min(mindiff , 1440 - li[-1] + li[0])
        
        return mindiff
