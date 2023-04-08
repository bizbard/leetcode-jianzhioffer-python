from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quicksort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and strs[i] + strs[l] <= strs[l] + strs[i]:
                    i += 1
                while i < j and strs[j] + strs[l] >= strs[l] + strs[j]:
                    j -= 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[l], strs[i] = strs[i], strs[l]

            quicksort(l, i-1)
            quicksort(i+1, r)

        strs = [str(num) for num in nums]
        quicksort(0, len(strs) - 1)
        return ''.join(strs)

if __name__ == '__main__':
    # ======= Test Case =======
    nums = [3,30,34,5,9]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.minNumber(nums)
    print(res)