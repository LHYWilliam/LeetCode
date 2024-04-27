#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.now, self.max = 0, 0
        pass

    def travel(self, root: Optional[TreeNode]) -> None:  # type: ignore
        self.now += 1
        self.max = max(self.now, self.max)

        if root.left:
            self.travel(root.left)

        if root.right:
            self.travel(root.right)

        self.now -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:  # type: ignore
        if root:
            self.travel(root)

        return self.max


# @lc code=end
