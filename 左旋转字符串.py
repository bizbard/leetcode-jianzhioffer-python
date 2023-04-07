from typing import List


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


if __name__ == '__main__':
    # ======= Test Case =======
    s = "abcdefg"
    k = 2
    # ====== Driver Code ======
    sol = Solution()
    res = sol.reverseLeftWords(s, k)
    print(res)