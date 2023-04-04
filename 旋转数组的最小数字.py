from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right-left)//2
            if numbers[mid] > numbers[right]:
                left = mid+1
            if numbers[mid] < numbers[right]:
                right = mid
            
        return numbers[left]


if __name__ == '__main__':
    # ======= Test Case =======
    numbers = [3,4,5,1,2]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.minArray(numbers)
    print(res)