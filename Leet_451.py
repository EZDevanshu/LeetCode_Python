class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        res = ""
        for i in s:
            if i not in di :
                di[i] = 1 
            else :
                di[i] += 1
            
        sorted_di = dict(sorted(di.items() , key = lambda x : x[1] , reverse = True))

        for k , v in sorted_di.items() :
            res += k
            while v != 1 :
                res += k
                v -= 1
        
        return res