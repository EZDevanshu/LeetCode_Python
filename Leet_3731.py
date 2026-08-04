class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)

        
        li = []
        start = mn 
        for i in range(mn , mx + 1) :
            if start not in nums :
                li.append(start)
            start+=1

        return li