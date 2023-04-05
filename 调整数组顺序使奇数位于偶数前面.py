from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        return nums


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3,4]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.exchange(nums)
    print(res)