from typing import List
import math

class Solution:
    # def cuttingRope(self, n: int) -> int:
    #     if n <= 3: return n - 1
    #     a, b = n // 3, n % 3
    #     if b == 0: return int(math.pow(3, a)) % 1000000007
    #     if b == 1: return int(math.pow(3, a - 1) * 4) % 1000000007
    #     return int(math.pow(3, a) * 2) % 1000000007

    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p # = 3^(a+1) % p
        if b == 1: return (rem * 4) % p # = 3^a * 4 % p
        return (rem * 6) % p # = 3^(a+1) * 2  % p



if __name__ == '__main__':
    # ======= Test Case =======
    n = 10
    # ====== Driver Code ======
    sol = Solution()
    res = sol.cuttingRope(n)
    print(res)