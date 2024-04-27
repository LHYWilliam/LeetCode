#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
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
        self.tree1, self.tree2 = [], []

    def travel(self, root, tree: list):
        tree.append(root.val)
        if root.left:
            self.travel(root.left, tree)
        else:
            tree.append(None)
        if root.right:
            self.travel(root.right, tree)
        else:
            tree.append(None)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  # type: ignore
        if p:
            self.travel(p, self.tree1)
        if q:
            self.travel(q, self.tree2)

        return self.tree1 == self.tree2


# @lc code=end
