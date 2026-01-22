from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for i in range(len(nums)):
            check = target - nums[i]

            if check in map1:
                return [map1[check], i]

            map1[nums[i]] = i

        return []
nums = [3, 2 , 4]
target = 6
obj = Solution()
print(obj.twoSum(nums , target))