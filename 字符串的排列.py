from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        # res = []
        # def dfs(s, path):
        #     if not s:
        #         res.append(path)
        #         return
        #     for i in range(len(s)):
        #         dfs(s[0:i]+s[i+1:], path+s[i])
        # dfs(s, '')
        # return res

        res = []
        def dfs(s, path):
            if len(path) == 3:
                res.append(path)
                return
            for i in range(len(s)):
                dfs(s, path+s[i])
        dfs(s, '')
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    s = "abc"
    # ====== Driver Code ======
    sol = Solution()
    res = sol.permutation(s)
    print(res)