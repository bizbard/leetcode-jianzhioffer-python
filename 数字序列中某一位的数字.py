from typing import List


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.


if __name__ == '__main__':
    # ======= Test Case =======
    n = 11
    # ====== Driver Code ======
    sol = Solution()
    res = sol.findNthDigit(n)
    print(res)