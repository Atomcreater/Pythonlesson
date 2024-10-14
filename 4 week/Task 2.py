#47. Permutations II
#https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=array
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            if index == size:
                permutations.append(current_permutation[:])
                return

            for j in range(size):
                if visited[j] or (j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]):
                    continue
                current_permutation[index] = nums[j]
                visited[j] = True
                backtrack(index + 1)
                visited[j] = False

        size = len(nums)
        nums.sort()
        permutations = []
        current_permutation = [0] * size
        visited = [False] * size

        backtrack(0)

        return permutations