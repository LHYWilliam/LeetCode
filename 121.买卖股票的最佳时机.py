#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # type: ignore
        prices = [{"day": day + 1, "price": price} for day, price in enumerate(prices)]

        profits = []
        for one in prices:
            temp = sorted(prices[one["day"] :], key=lambda one: -one["price"])

            profits.append(temp[0]["price"] - one["price"] if temp else 0)

        return max(profits)


# @lc code=end
