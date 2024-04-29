#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(i) for i in f"{bin(n)}"[2:]])


# @lc code=end
