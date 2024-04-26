#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  # type: ignore
        if all([one == 9 for one in digits]):
            digits = [1] + [0 for _ in range(len(digits))]
        else:
            digits[-1] += 1
            for i in range(len(digits) - 1, 0, -1):
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i - 1] += 1

        return digits


# @lc code=end
