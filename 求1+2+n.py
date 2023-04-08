from typing import List


class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    # ======= Test Case =======
    n = 3
    # ====== Driver Code ======
    sol = Solution()
    res = sol.sumNums(n)
    print(res)