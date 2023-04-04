from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = set()
        for num in nums:
            if num in dic:
                return num
            dic.add(num)
        return -1


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [2, 3, 1, 0, 2, 5, 3]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.findRepeatNumber(nums)
    print(res)