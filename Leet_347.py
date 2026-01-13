class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        res = []

        for i in nums:
            if not i in di :
                di[i] = 1
            else :
                di[i] += 1
        sorted_dict = sorted(di.items(), key = lambda x : x[1] , reverse = True)

        res = [i[0] for i in sorted_dict[:k]] 
        return res