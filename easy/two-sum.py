# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        indices = {}
        for idx, num in enumerate(nums):
            if num not in indices:
                indices[num] = [idx]
            else:
                indices[num].append(idx)
        print(indices, len(indices[3]))
        for num in indices:
            if num*2 == target:
                if len(indices[num]) > 1:
                    return indices[num][:2]
            elif target - num in indices:
                return [indices[num][0], indices[target - num][0]]