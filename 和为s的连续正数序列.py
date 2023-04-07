from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j+1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    target = 9
    # ====== Driver Code ======
    sol = Solution()
    res = sol.findContinuousSequence(target)
    print(res)