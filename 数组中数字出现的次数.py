from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1       
        for num in nums:         # 3. 遍历 nums 分组
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字



if __name__ == '__main__':
    # 两个相同数字异或为 0
    # ======= Test Case =======
    nums = [1,2,10,4,1,4,3,3]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.singleNumbers(nums)
    print(res)