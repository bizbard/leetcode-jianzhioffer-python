from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        while i < len(pushed) and j < len(popped):
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
            else:
                stack.append(pushed[i])
                while stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
            i += 1
        
        return True if not stack else False


if __name__ == '__main__':
    # ======= Test Case =======
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.validateStackSequences(pushed, popped)
    print(res)