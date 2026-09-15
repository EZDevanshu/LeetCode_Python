class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        di  = {}

        for i in range(len(arr)) :
            if target - arr[i] in di : 
                return [di[target - arr[i]] + 1 , i + 1]
            else :
                di[arr[i]] = i

        return [0,0] 
        
