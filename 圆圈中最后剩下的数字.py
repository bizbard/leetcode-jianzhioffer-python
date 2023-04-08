from typing import List


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x


if __name__ == '__main__':
    # ======= Test Case =======
    n = 5
    m = 3
    # ====== Driver Code ======
    sol = Solution()
    res = sol.lastRemaining(n, m)
    print(res)