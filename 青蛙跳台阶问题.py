from typing import List


class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        sum = 0
        for i in range(n):
            sum = a + b
            a = b
            b = sum

        return a % 1000000007


if __name__ == '__main__':
    # ======= Test Case =======
    n = 5
    # ====== Driver Code ======
    sol = Solution()
    res = sol.numWays(n)
    print(res)