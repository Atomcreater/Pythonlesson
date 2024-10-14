#46. Permutations
#https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=array
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index):
            if index == len_nums:
                permutations.append(current_permutation[:])
                return

            for j in range(len_nums):

                if not visited[j]:
                    visited[j] = True
                    current_permutation[index] = nums[j]

                    backtrack(index + 1)
                    visited[j] = False

        len_nums = len(nums)
        visited = [False] * len_nums
        current_permutation = [0] * len_nums
        permutations = []
        backtrack(0)
        return permutations