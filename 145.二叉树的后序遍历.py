#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
        self.answer = []

    def travel(self, root):
        if root.left:
            self.travel(root.left)
        if root.right:
            self.travel(root.right)

        self.answer.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # type: ignore
        if root:
            self.travel(root)

        return self.answer


# @lc code=end
