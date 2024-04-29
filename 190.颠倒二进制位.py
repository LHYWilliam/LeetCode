#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n = f"{bin(n)}"[2:]
        n = "0" * (32 - len(n)) + n
        answer = eval("0b" + "".join(list(reversed(n))))
        return answer


# @lc code=end
