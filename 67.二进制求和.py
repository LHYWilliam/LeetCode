#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a = [0 for _ in range(maxlen - len(a))] + [int(one) for one in a]
        b = [0 for _ in range(maxlen - len(b))] + [int(one) for one in b]
        answer = [0 for _ in range(maxlen)]

        for i in range(maxlen - 1, 0 - 1, -1):
            answer[i] = a[i] + b[i] + answer[i]
            if answer[i] > 1 and i != 0:
                answer[i - 1 : i + 1] = [1, answer[i] % 2]

        if answer[0] > 1:
            answer = [1, answer[0] % 2] + answer[1:]

        answer = "".join([str(one) for one in answer])
        return answer


# @lc code=end
