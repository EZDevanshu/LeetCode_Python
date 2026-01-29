class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        Sp , Tp = 0 , 0

        while Sp < len(s) and Tp < len(t) :
            if s[Sp] == t[Tp] :
                Sp += 1
            Tp += 1

        return Sp == len(s)
                
