from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(l, r):
            if l >= r:
                return 0
            m = (l+r)//2
            res = mergesort(l, m) + mergesort(m+1, r)
            i, j = l, m+1
            tmp[l:r+1] = nums[l:r+1]
            for k in range(l, r+1):
                if i == m+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m-i+1
            return res
        
        tmp = [0] * len(nums)
        return mergesort(0, len(nums)-1)


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [7,5,6,4]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.reversePairs(nums)
    print(res)