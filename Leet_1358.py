class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        j = 0 
        ans = 0
        aC = 0
        bC = 0 
        cC = 0

        while j < len(s):
            
            if s[j] == 'a' :
                aC += 1
            elif s[j] == 'b' :
                bC += 1
            elif s[j] == 'c' :
                cC += 1
            
            while aC > 0 and bC > 0 and cC > 0 :
                
                ans += len(s) - j 
                if s[i] == 'a' :
                    aC -= 1
                elif s[i] == 'b' :
                    bC -= 1
                elif s[i] == 'c' :
                    cC -= 1
                
                i += 1
            else :
                j += 1
            
        return ans 