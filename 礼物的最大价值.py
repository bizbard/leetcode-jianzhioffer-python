from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        p = [0 for i in range(len(grid))]
        for i in range(len(grid)):
            p[i] = [0 for i in range(len(grid[0]))]

        p[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            p[i][0] = p[i-1][0] + grid[i][0]

        for j in range(1, len(grid[0])):
            p[0][j] = p[0][j-1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                p[i][j] = max((p[i][j-1] + grid[i][j]), (p[i-1][j] + grid[i][j]))
        
        return p[-1][-1]


if __name__ == '__main__':
    # ======= Test Case =======
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.maxValue(grid)
    print(res)