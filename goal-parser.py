# https://leetcode.com/problems/goal-parser-interpretation/

import sys

class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result.append(command[i])
                i += 1
                continue
            if command[i] == '(':
                if i == len(command) - 1:
                    sys.exit(1)
                if command[i+1] == ')':
                    result.append('o')
                    i += 2
                    continue
                if i + 3 > len(command) - 1:
                    sys.exit(1)
                if command[i:i+4] == '(al)':
                    result.append('al')
                    i += 4
                    continue
        return ''.join(result)
