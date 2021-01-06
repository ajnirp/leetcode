# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_length = len(nums) // 2
        left = nums[0:half_length]
        right = nums[half_length:]
        result = []
        for l, r in zip(left, right):
            result.append(l)
            result.append(r)
        return result