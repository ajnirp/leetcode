# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result = [nums[0]]
        for num in nums[1:]:
            result.append(result[-1] + num)
        return result