from typing import List


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else: res.append(c)
        return ''.join(res)


if __name__ == '__main__':
    # ======= Test Case =======
    s = "We are happy."
    # ====== Driver Code ======
    sol = Solution()
    res = sol.replaceSpace(s)
    print(res)