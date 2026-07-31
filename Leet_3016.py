class Solution:
    def minimumPushes(self, word: str) -> int:
        di = Counter(word)

        sorted_di = dict(sorted(di.items() , key = lambda x : x[1],reverse = True))

        totalCost = 0
        i = 1
        count = 8 

        for k, v in sorted_di.items() :
            totalCost += v * i
            count-= 1
            if count == 0 :
                count = 8
                i+= 1

        return totalCost  
