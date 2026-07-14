class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = max(weights)
        e = sum(weights)

        while(s <= e) :
            count = 1
            total = 0
            mid = s + (e - s) // 2
            for i in range(0, len(weights)) :
                if total + weights[i] > mid :
                    count += 1
                    total = 0
                total += weights[i]
            if count <= days :
                e = mid - 1     
            elif count > days :
                s = mid + 1 

        return s 


                       
