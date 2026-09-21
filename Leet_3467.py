class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        oddCnt = 0
        result = list()
        for num in nums:
            if num % 2 == 0:
                result.append(0)
            else:
                oddCnt+=1
        while oddCnt > 0:
            result.append(1)
            oddCnt-=1
        return result