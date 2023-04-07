from typing import List
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        dic = collections.defaultdict(int)
        dic[s[0]] = 1
        for j in range(1, len(s)):
            if dic[s[j]]:
                while dic[s[j]]:
                    dic[s[i]] -= 1
                    i += 1
                dic[s[j]] += 1
            else:
                dic[s[j]] += 1
            res = max(res, j-i+1)
        return res


if __name__ == '__main__':
    # ======= Test Case =======
    s = "au"
    # ====== Driver Code ======
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)