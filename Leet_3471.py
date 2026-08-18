class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        di = Counter()
        
        for i in range(len(nums) - k + 1):
            for j in set(nums[i:i+k]):
                di[j] += 1

            
            mx = -1
            for i in di :
                if di[i] == 1 :
                    mx = max(mx , i)

        return mx 