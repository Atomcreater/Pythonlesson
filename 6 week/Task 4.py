#2653. Sliding Subarray Beauty
#https://leetcode.com/problems/sliding-subarray-beauty/description/?envType=problem-list-v2&envId=sliding-window
from sortedcontainers import SortedList
from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sorted_list = SortedList(nums[:k])

        result = [sorted_list[x - 1] if sorted_list[x - 1] < 0 else 0]

        for i in range(k, len(nums)):
            sorted_list.remove(nums[i - k])
            sorted_list.add(nums[i])

            result.append(sorted_list[x - 1] if sorted_list[x - 1] < 0 else 0)

        return result