from typing import List


class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [0] * (len(num)+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(num)+1):
            if 0 <= int(num[i-2] + num[i-1]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    # ======= Test Case =======
    num = 12258
    # ====== Driver Code ======
    sol = Solution()
    res = sol.translateNum(num)
    print(res)