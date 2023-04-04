from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    n = 11
    # ====== Driver Code ======
    sol = Solution()
    res = sol.hammingWeight(n)
    print(res)