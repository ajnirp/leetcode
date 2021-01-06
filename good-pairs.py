# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i] == nums[j] for i in range(len(nums)) for j in range(i+1, len(nums)))