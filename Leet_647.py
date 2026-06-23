# brute force approch 

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         li = []

#         for i in range(len(s)) :
#             res = ""
#             for j in range(i , len(s)) :
#                 res += s[j]
#                 li.append(res)

#         count = 0
#         for x in li :
#             if x[::-1] == x :
#                 count += 1    

#         return count  


# optimal approch 

class Solution:
    def countSubstrings(self, s: str) -> int :
        count = 0

        def checkPalindrome(l , r) :
            noOfPalin = 0
            while l >= 0 and r < len(s) and s[l] == s[r] :
                noOfPalin += 1
                l -= 1
                r += 1

            return noOfPalin
        
        for i in range(len(s)) :
            count += checkPalindrome(i , i)
            count += checkPalindrome(i , i + 1)

        return count
    
      
     
      