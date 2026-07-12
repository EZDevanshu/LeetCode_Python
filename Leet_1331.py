class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        di1 = {}
        di2 = {}

        temp = arr[:]  

        for i in range(len(arr)):
            if arr[i] in di1:
                continue
            di1[arr[i]] = i

        arr.sort()

        rank = 1
        for i in range(len(arr)):
            if arr[i] in di2:
                continue
            di2[arr[i]] = rank
            rank += 1

        li = []

        for i in range(len(temp)):
            li.append(di2[temp[i]])

        return li