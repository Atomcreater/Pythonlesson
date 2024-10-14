#85. Maximal Rectangle
#https://leetcode.com/problems/maximal-rectangle/description/?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for col_idx, val in enumerate(row):
                if val == "1":

                    heights[col_idx] += 1
                else:

                    heights[col_idx] = 0

            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:

        num_heights = len(heights)
        stack = []
        prev_smaller = [-1] * num_heights
        next_smaller = [num_heights] * num_heights

        for i, height in enumerate(heights):

            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(num_heights - 1, -1, -1):
            cur_height = heights[i]
            while stack and heights[stack[-1]] >= cur_height:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        max_area = max(
            height * (next_smaller[i] - prev_smaller[i] - 1) for i, height in enumerate(heights)
        )

        return max_area