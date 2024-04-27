#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:

    # def climbStairs(self, n: int) -> int:
    #     from queue import Queue

    #     answer = 0
    #     plan = Queue()
    #     if n - 0 >= 1:
    #         plan.put(0 + 1)
    #     if n - 0 >= 2:
    #         plan.put(0 + 2)

    #     while not plan.empty():
    #         next = plan.get()
    #         if next == n:
    #             answer += 1

    #         if n - next >= 1:
    #             plan.put(next + 1)
    #         if n - next >= 2:
    #             plan.put(next + 2)

    #     return answer

    # def __init__(self):
    #     self.goal = 0
    #     self.answer = 0

    # def step(self, goal, now, step):
    #     now = now + step
    #     if now == goal:
    #         self.answer += 1

    #     if now + 1 <= goal:
    #         self.step(goal, now, 1)
    #     if now + 2 <= goal:
    #         self.step(goal, now, 2)

    # def climbStairs(self, n: int) -> int:
    #     self.step(n, 0, 1)
    #     self.step(n, 0, 2)

    #     return self.answer

    def climbStairs(self, n: int) -> int:
        answer = [0 for _ in range(n + 1)]
        answer[1] = 1
        if n >= 2:
            answer[2] = 2
        for i in range(3, n + 1):
            answer[i] = answer[i - 1] + answer[i - 2]

        return answer[n]


# @lc code=end
