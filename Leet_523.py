class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = []
        cur = 0

        for i in nums :
            cur += i
            prefixSum.append(cur)
        
        di = {0 : -1}

        for i in range(len(prefixSum)) : 
            rem = prefixSum[i] % k 
            if rem in di :
                if i - di[rem] >= 2 :
                    return True
            else :
                di[rem] = i
        return False 