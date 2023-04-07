from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)