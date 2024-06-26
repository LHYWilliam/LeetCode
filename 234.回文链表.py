#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:  # type: ignore
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        return vals == list(reversed(vals))


# @lc code=end
