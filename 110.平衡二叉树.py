#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:  # type: ignore
        left = self.depth(root.left) if root.left else 0
        right = self.depth(root.right) if root.right else 0

        return 1 + max(left, right)

    def balabced(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        if not root:
            flag = True
        elif not root.left and not root.right:
            flag = True
        elif root.left and root.right:
            flag = (self.depth(root.left) - self.depth(root.right)) in (-1, 0, 1)
        else:
            flag = (
                self.depth(root.left) == 1 if root.left else self.depth(root.right) == 1
            )

        return flag

    def isBalanced(self, root: Optional[TreeNode]) -> bool:  # type: ignore
        return (
            self.balabced(root)
            and (self.isBalanced(root.left) if root else True)
            and (self.isBalanced(root.right) if root else True)
        )


# @lc code=end
