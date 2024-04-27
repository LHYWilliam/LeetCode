#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
        self.answer.append(root.val)
        if root.right:
            self.travel(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # type: ignore
        if root:
            self.travel(root)

        return self.answer


# @lc code=end
