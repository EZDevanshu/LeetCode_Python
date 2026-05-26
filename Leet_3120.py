class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)

        count = 0

        for i in range(26) :
            l = chr(ord('a') + i)
            u = chr(ord('A') + i)

            if l in s and u in s :
                count += 1
        return count 
    