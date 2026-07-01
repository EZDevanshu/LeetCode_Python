class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        total = sum(arr[:k])
        avg = total // k

        if avg >= threshold :
            count += 1

        i = 1
        j = k

        while j < len(arr) :
            total -= arr[i - 1]
            total += arr[j]

            avg = total // k

            if avg >= threshold :
                count += 1
            i += 1
            j += 1
        return count 
