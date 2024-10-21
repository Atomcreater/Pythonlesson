#229. Majority Element II
#https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=hash-table
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [m for m in (candidate1, candidate2) if nums.count(m) > len(nums) // 3]