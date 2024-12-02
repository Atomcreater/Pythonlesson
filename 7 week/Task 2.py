#413. Arithmetic Slices
#https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window
from itertools import pairwise


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_slices = 0
        current_sequence_length = 0

        previous_difference = 3000

        for current_num, next_num in pairwise(nums):
            current_difference = next_num - current_num

            if current_difference == previous_difference:
                current_sequence_length += 1
            else:
                previous_difference = current_difference
                current_sequence_length = 0

            total_slices += current_sequence_length

        return total_slices