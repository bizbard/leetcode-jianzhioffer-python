from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 1
            if target - nums[i] in dic:
                return [nums[i], target-nums[i]]
            else:
                continue
        return [-1, -1]


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [2,7,11,15]
    target = 9
    # ====== Driver Code ======
    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)