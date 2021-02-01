# https://leetcode.com/problems/single-row-keyboard

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        chars = [0] + [keyboard.index(c) for c in word]
        print(chars)
        sum_ = 0
        for i in range(1, len(chars)):
            sum_ += abs(chars[i] - chars[i-1])
        return sum_

