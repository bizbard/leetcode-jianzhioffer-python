from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(nums)
        m = len(nums[0])

        j = 0
        i = n-1
        while 0 <= i and j <= n-1:
            if nums[j][i] < target:
                j += 1
                continue
            if nums[j][i] > target:
                i -= 1
                continue
            if nums[j][i] == target:
                return True
        else:
            return False

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
    target = 20
    # ====== Driver Code ======
    sol = Solution()
    res = sol.findNumberIn2DArray(nums, target)
    print(res)