from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    # dp[i] 代表以元素 nums[i]nums[i]nums[i] 为结尾的连续子数组最大和。
    # 为何定义最大和 dp[i]dp[i]dp[i] 中必须包含元素 nums[i]nums[i]nums[i] ：保证 dp[i]dp[i]dp[i] 递推到 dp[i+1]dp[i+1]dp[i+1] 的正确性；如果不包含 nums[i]nums[i]nums[i] ，递推时则不满足题目的 连续子数组 要求。

    # ======= Test Case =======
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.maxSubArray(nums)
    print(res)