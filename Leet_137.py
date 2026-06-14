class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        di = {}

        for i in arr :
            if i in di :
                di[i] += 1
            else :
                di[i] = 1

        for i , j in di.items() :
            if di[i] == 1 :
                return i