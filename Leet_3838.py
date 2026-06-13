class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        add = ""
        for word in words :
            total = 0
            for i in word :
                total += weights[ord(i) - ord('a')]

            add += chr(ord('a') + 25 - (total % 26))
        return add
            
            