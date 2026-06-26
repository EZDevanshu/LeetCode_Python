# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2) :
#             return False

#         d1 = {}
#         d2 = {}

#         for i in range(len(word1)) :
#             d1[word1[i]] = d1.get(word1[i] , 0) + 1
        
#         for i in range(len(word2)) :
#             d2[word2[i]] = d2.get(word2[i] , 0) + 1
           
#         if set(d1.keys()) != set(d2.keys()) :
#             return False 
        
#         if sorted(d1.values()) != sorted(d2.values()) :
#             return False
         
#         return True 

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) :
            return False

        d1 = Counter(word1)
        d2 = Counter(word2)
           
        return (
            set(d1.keys()) == set(d2.keys())
            and
            sorted(d1.values()) == sorted(d2.values())
        )