from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==0:
            return 0
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)
        
        return dp[-1]


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [7,1,5,3,6,4]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)