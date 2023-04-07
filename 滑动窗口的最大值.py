from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque(nums[:k])
        res = [max(queue)]
        j = k
        while j < len(nums):
            queue.popleft()
            queue.append(nums[j])
            res.append(max(queue))
            j += 1
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # ====== Driver Code ======
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print(res)