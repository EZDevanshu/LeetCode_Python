class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))
        t = list(str(num))
        x = None
        falg = False

        # maximum
        for i in range(len(s)) :
            if s[i] != '9' :
                x = s[i]
                s[i] = '9'
                break 
        if x is not None :
            for i in range(len(s)) :
                if s[i] == x :
                    s[i] = '9'
        
        a = int("".join(s))

        x = None 
    
        if t[0] != '1' :
            x = t[0]
            t[0] = '1'
            falg = True
        
        # minimum
        if not falg :
            for i in range(len(t)):
                if t[i] != '0' and t[i] != '1':
                    x = t[i]
                    t[i] = '0'
                    break   
        if x is not None :
            for i in range(len(t)) :
                if not falg :
                    if t[i] == x :
                        t[i] = '0'
                else :
                    if t[i] == x :
                        t[i] = '1'

        b = int("".join(t))

        return a - b