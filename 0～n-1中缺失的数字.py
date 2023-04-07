from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [0,1,2,3,4,5,6,7,9]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.missingNumber(nums)
    print(res)