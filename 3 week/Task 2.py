#15. 3Sum
#https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=array
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []

        for i in range(n - 2):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1

                elif current_sum > 0:
                    right -= 1

                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets