#164. Maximum Gap
#https://leetcode.com/problems/maximum-gap/description/?envType=problem-list-v2&envId=array
from math import inf

class Solution:
    def maximumGap(self, nums):

        num_elements = len(nums)

        if num_elements < 2:
            return 0

        min_val, max_val = min(nums), max(nums)

        bucket_size = max(1, (max_val - min_val) // (num_elements - 1))

        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[inf, -inf] for _ in range(bucket_count)]

        for value in nums:
            bucket_index = (value - min_val) // bucket_size
            buckets[bucket_index][0] = min(buckets[bucket_index][0], value)
            buckets[bucket_index][1] = max(buckets[bucket_index][1], value)

        max_gap = 0

        previous_max = inf

        for current_min, current_max in buckets:
            if current_min > current_max:
                continue

            max_gap = max(max_gap, current_min - previous_max)

            previous_max = current_max

        return max_gap