#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
        self.left, self.right = [], []

    def leftTravel(self, root: Optional[TreeNode], result: list) -> None:  # type: ignore
        result.append(root.val)

        if root.left:
            self.leftTravel(root.left, result)
        else:
            result.append(None)

        if root.right:
            self.leftTravel(root.right, result)
        else:
            result.append(None)

    def rightTravel(self, root: Optional[TreeNode], result: list) -> None:  # type: ignore
        result.append(root.val)

        if root.right:
            self.rightTravel(root.right, result)
        else:
            result.append(None)

        if root.left:
            self.rightTravel(root.left, result)
        else:
            result.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        if root.left:
            self.leftTravel(root.left, self.left)
        if root.right:
            self.rightTravel(root.right, self.right)

        return self.left == self.right


# @lc code=end
