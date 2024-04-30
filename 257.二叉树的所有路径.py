#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:  # type: ignore
        from queue import Queue

        nodes = Queue()
        nodes.put((root, f"{root.val}"))

        answer = []
        while not nodes.empty():
            node, path = nodes.get()

            if not node.left and not node.right:
                answer.append(path)

            if node.left:
                nodes.put((node.left, path + f"->{node.left.val}"))
            if node.right:
                nodes.put((node.right, path + f"->{node.right.val}"))

        return answer


# @lc code=end
