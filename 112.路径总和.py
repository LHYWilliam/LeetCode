#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  # type: ignore
        from queue import Queue

        nodes = Queue()
        if root:
            nodes.put((root, root.val))

        flag = False
        while not nodes.empty():
            node, sum = nodes.get()

            if node:
                if not node.left and not node.right and sum == targetSum:
                    flag = True
                    break

                if node.left:
                    nodes.put((node.left, sum + node.left.val))
                if node.right:
                    nodes.put((node.right, sum + node.right.val))

        return flag


# @lc code=end
