class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        i = 0 
        j = 0
        count = 0
        p.sort()
        t.sort()
        while (i != len(p) and j != len(t)) :
            if p[i] <= t[j] :
                count+= 1
                i+=1 

            j+=1
        return count 
            