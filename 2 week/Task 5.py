#139. Word Break
#https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=string
class Solution:
    def wordBreak(self, s: str, word_set: List[str]) -> bool:
        words = set(word_set)

        length_of_s = len(s)

        can_break = [True] + [False] * length_of_s

        for i in range(1, length_of_s + 1):
            can_break[i] = any(can_break[j] and s[j:i] in words for j in range(i))

        return can_break[length_of_s]