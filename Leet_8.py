class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        clean = s.strip()
        i = 0

        if not clean :
            return 0

        if clean[0] == '-' :
            sign = -1
            i += 1
        elif clean[0] == '+' :
            i += 1
    
        num = 0

        while i < len(clean) and clean[i].isdigit():
                num = num * 10 + int(clean[i])

                if sign * num > 2**31 - 1 :
                    return 2**31 - 1
                if sign * num < -2**31 :
                    return -2**31

                i += 1
            
        return num * sign