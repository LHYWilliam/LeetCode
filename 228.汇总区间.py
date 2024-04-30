#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:  # type: ignore
        answer = []

        temp = ""
        for i in range(len(nums)):
            if not temp:
                temp = f"{nums[i]}"
            elif temp.find("->") == -1 and nums[i - 1] + 1 == nums[i]:
                temp = temp + f"->{nums[i]}"
            elif temp.find("->") != -1 and nums[i - 1] + 1 == nums[i]:
                temp = temp[: temp.find("->") + 2] + f"{nums[i]}"
            else:
                answer.append(temp)
                temp = f"{nums[i]}"
        if nums:
            answer.append(temp if temp else f"{nums[-1]}")

        return answer


# @lc code=end
