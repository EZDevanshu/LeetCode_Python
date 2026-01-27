class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        i , j = 0 , 1
        profit = 0
        while j < len(arr):
            if arr[j] > arr[i]:
                profit = max(arr[j] - arr[i] , profit)
            else :
                i = j
            j += 1
        return profit 