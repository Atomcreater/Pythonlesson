#5. Longest Palindromic Substring
#https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=string

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_pal_substr(s):
            n = len(s)
            if n == 0:
                return ""

            start = 0
            max_len = 1

            for i in range(n):

                for j in range(2):
                    low = i
                    hi = i + j

                    while low >= 0 and hi < n and s[low] == s[hi]:
                        curr_len = hi - low + 1
                        if curr_len > max_len:
                            start = low
                            max_len = curr_len
                        low -= 1
                        hi += 1

            return s[start:start + max_len]

        return (longest_pal_substr(s))
