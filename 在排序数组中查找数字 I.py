from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, target, lower):
            left = 0
            right = len(nums) - 1
            ans = len(nums)
            if lower:
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] >= target:
                        right = mid - 1
                        ans = mid
                    else:
                        left = mid + 1
                return ans
            else:
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] > target:
                        right = mid - 1
                        ans = mid - 1
                    else:
                        left = mid + 1
                return ans

        leftIdx = binarySearch(nums, target, True)
        rightIdx = binarySearch(nums, target, False)
        if leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
            return rightIdx-leftIdx+1
        else:
            return 0


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [5,7,7,8,8,10]
    target = 8
    # ====== Driver Code ======
    sol = Solution()
    res = sol.search(nums, target)
    print(res)