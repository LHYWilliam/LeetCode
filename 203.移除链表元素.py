#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:  # type: ignore
        temp = head
        while temp and temp.next:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next

            temp = temp.next

        if head and head.val == val:
            head = head.next

        return head


# @lc code=end
