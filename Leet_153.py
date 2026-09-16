class Solution:
    def findMin(self, arr: list[int]) -> int:
        s = 0 
        e = len(arr) - 1

        while s < e :
            mid = s + (e - s) // 2 

            if arr[mid] > arr[e] :
                s = mid + 1
            else :
                e = mid 

        return arr[s]