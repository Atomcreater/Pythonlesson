#72. Edit Distance
#https://leetcode.com/problems/edit-distance/description/?envType=problem-list-v2&envId=string
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def edit_dist(s1, s2):
            m, n = len(s1), len(s2)
            prev = 0
            curr = list(range(n + 1))

            for i in range(1, m + 1):
                prev = curr[0]
                curr[0] = i
                for j in range(1, n + 1):
                    temp = curr[j]
                    if s1[i - 1] == s2[j - 1]:
                        curr[j] = prev
                    else:
                        curr[j] = 1 + min(curr[j - 1], prev, curr[j])
                    prev = temp
            return curr[n]


        return(edit_dist(word1, word2))