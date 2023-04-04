from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(10^(n-1)):
            res.append(i)           
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    n = 1
    # ====== Driver Code ======
    sol = Solution()
    res = sol.printNumbers(n)
    print(res)