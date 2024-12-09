#124. Binary Tree Maximum Path Sum
#https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=problem-list-v2&envId=binary-tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left_max = max(0, dfs(node.left))

            right_max = max(0, dfs(node.right))

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        max_path_sum = float('-inf')

        dfs(root)

        return max_path_sum
