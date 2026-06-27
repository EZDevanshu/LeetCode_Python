class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        li = []
        tot = 0
        res = ""
        for i in range(len(shifts) - 1 , -1 , -1) :
            tot += shifts[i]
            li.append(tot)

        li.reverse()

        for i in range(len(s)) :
            res += chr((ord(s[i]) - ord('a') + li[i]) % 26 + ord('a'))  
           
        return res
