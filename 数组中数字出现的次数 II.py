from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 3):
            if i >= len(nums)-1 or nums[i] != nums[i+1]:
                if i >= len(nums)-1:
                    return nums[nums.length-1]
                else:
                    return nums[i]
        return -1



if __name__ == '__main__':
    # 两个相同数字异或为 0
    # ======= Test Case =======
    nums = [9,1,7,9,7,9,7]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.singleNumber(nums)
    print(res)