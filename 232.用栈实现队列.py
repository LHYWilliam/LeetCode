#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#


# @lc code=start
class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        data = self.data[0]
        del self.data[0]

        return data

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
