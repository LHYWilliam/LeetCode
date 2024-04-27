#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left * left < x and right * right > x:
            if left * left < x:
                left += 1
            if right * right > x:
                right -= 1

        if left * left > x:
            answer = left - 1
        elif left * left == x:
            answer = left
        if right * right <= x:
            answer = right

        return answer


# @lc code=end
