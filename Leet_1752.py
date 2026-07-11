class Solution:
    def check(self, arr: List[int]) -> bool:
        i = 1
        count = 0
        while(i < len(arr)) :
            if not arr[i - 1] <= arr[i] :
                count += 1

            if count > 1 :
                return False
            
            i+=1
        
        if arr[-1] > arr[0] :
            count += 1
        
        return count <= 1