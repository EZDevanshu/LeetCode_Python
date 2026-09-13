class Solution:
    def sortString(self, s: str) -> str:
        res = ''

        li = list(s)

        while li:
            for i in sorted(set(li)) :
                li.remove(i)
                res += i

            for x in sorted(set(li) , reverse=True) :
                li.remove(x)
                res += x
            
        return res