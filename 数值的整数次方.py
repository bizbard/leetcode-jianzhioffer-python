from typing import List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n<0:
            x, n = 1/x, -n
        res = 1
        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1 
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    x = 2.00000
    n = 10
    # ====== Driver Code ======
    sol = Solution()
    res = sol.myPow(x, n)
    print(res)