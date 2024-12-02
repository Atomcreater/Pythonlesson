#1499. Max Value of Equation
#https://leetcode.com/problems/max-value-of-equation/description/?envType=problem-list-v2&envId=sliding-window
from collections import deque
from math import inf


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = -inf

        candidates = deque()

        for x, y in points:
            while candidates and x - candidates[0][0] > k:
                candidates.popleft()

            if candidates:
                max_value = max(max_value, x + y + candidates[0][1] - candidates[0][0])

            while candidates and y - x >= candidates[-1][1] - candidates[-1][0]:
                candidates.pop()

            candidates.append((x, y))

        return max_value