# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]
        for interval in intervals[1:]:
            a, b = stack[-1]
            c, d = interval
            if c <= b:
                stack.pop()
                stack.append([a, max(b, d)])
            else:
                stack.append(interval)

        return stack