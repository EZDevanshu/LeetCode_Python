class Solution:
    def countValidPrefixes(self, s: str) -> int:
        ZC = 0
        OC = 0
        totalValid = 0
        i = 0
        for j in range(len(s)) :
            if s[j] == '0' :
                ZC += 1
            else :
                OC += 1

            if abs(ZC - OC) <= 1 :
                totalValid += 1

        return totalValid