#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        temp = head

        while temp and temp.next:
            while temp and temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            temp = temp.next

        return head


# @lc code=end
