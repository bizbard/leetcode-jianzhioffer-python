from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = c in dic
        for c in s:
            if not dic[c]:
                return c
        return ''


if __name__ == '__main__':
    # ======= Test Case =======
    s = "abaccdeff"
    # ====== Driver Code ======
    sol = Solution()
    res = sol.firstUniqChar(s)
    print(res)