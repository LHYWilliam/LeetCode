#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def travel(self, root):
        self.answer += 1

        if root.left:
            self.travel(root.left)
        if root.right:
            self.travel(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:  # type: ignore
        if root:
            self.travel(root)

        return self.answer


# @lc code=end
