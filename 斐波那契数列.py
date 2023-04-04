from typing import List


class Solution:
    def fib(self, n: int) -> int:
        f = [0 for _ in range(n+1)]
        if n == 0: return 0
        if n == 1: return 1
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n] % 1000000007


if __name__ == '__main__':
    # ======= Test Case =======
    n = 5
    # ====== Driver Code ======
    sol = Solution()
    res = sol.fib(n)
    print(res)