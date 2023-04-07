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

# # 单调栈  
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         deque = collections.deque()
#         res, n = [], len(nums)
#         for i, j in zip(range(1 - k, n + 1 - k), range(n)):
#             # 删除 deque 中对应的 nums[i-1]
#             if i > 0 and deque[0] == nums[i - 1]:
#                 deque.popleft()
#             # 保持 deque 递减
#             while deque and deque[-1] < nums[j]:
#                 deque.pop()
#             deque.append(nums[j])
#             # 记录窗口最大值
#             if i >= 0:
#                 res.append(deque[0])
#         return res


if __name__ == '__main__':
    # ======= Test Case =======
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # ====== Driver Code ======
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print(res)