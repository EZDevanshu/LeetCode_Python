class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        li = []

        for i in range(0 , len(nums), 2) :
            li.append(int(str(nums[i]) + str(nums[i + 1])))


        return min(li)