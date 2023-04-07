from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = len(s) - 1
        j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': 
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


if __name__ == '__main__':
    # ======= Test Case =======
    s = "the sky is blue"
    # ====== Driver Code ======
    sol = Solution()
    res = sol.reverseWords(s)
    print(res)