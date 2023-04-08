from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        first = 1
        res = [0] * len(nums)
        for i in range(1, len(nums)):
            first *= nums[i]
        res[0] = first
        for i in range(1, len(nums)):
            res[i] = res[i-1] // nums[i] * nums[i-1]
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,2,3,4,5]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.constructArr(nums)
    print(res)