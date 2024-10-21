#140. Word Break II
#https://leetcode.com/problems/word-break-ii/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start_index, path):
            if start_index == len(s):
                ans.append(" ".join(path))
                return
            for end_index in range(start_index, len(s)):
                w = s[start_index:end_index + 1]
                if w in wordDict:
                    path.append(w)
                    dfs(end_index + 1, path)
                    path.pop()

        ans = []
        dfs(0, [])
        return ans
