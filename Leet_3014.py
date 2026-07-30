class Solution:
    def minimumPushes(self, word: str) -> int:
        inc = 1
        total = 0
        for i in range(len(word)) :
            if i > 0 and i % 8 == 0:
                inc += 1
            
            total += inc
        return total 