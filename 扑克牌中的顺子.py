from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                return False
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat:
                return False
            repeat.add(num)
        
        return ma - mi < 5


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3,4,5]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.isStraight(nums)
    print(res)