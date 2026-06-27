class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVow = 0
        vowels = "aeiou"
        
        curCount = 0

        for x in range(0 , k) :
            if s[x] in vowels :
                curCount += 1
        maxVow = curCount 
        i = 0 
        j = k 
        while(j < len(s)) :
            if s[j] in vowels :
                curCount += 1

            if s[i] in vowels  :
                curCount -= 1
            
            maxVow = max(maxVow , curCount)
            j+= 1
            i+= 1
        return maxVow