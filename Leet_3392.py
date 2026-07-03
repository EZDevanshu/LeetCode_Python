class Solution:
    def countSubarrays(self, arr: List[int]) -> int:
        count = 0
        i = 0
        j = 2
        while j < len(arr):
            if (arr[j - 2] + arr[j]) * 2 == arr[j - 1] :
                count += 1
            i += 1
            j += 1
        
        return count