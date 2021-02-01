# https://leetcode.com/problems/most-common-word/

from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = paragraph.split()
        counts = Counter()
        max_count, most_common_word = 0, ''
        for word in words:
            word = word.lower()
            if not word[-1].isalpha():
                word = word[:-1]
            if word in banned:
                continue
            counts[word] += 1
            if counts[word] > max_count:
                max_count = counts[word]
                most_common_word = word
        return most_common_word