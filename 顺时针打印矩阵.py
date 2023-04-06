from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1
        res = []
        while True:
            for i in range(l, r+1): # left to right
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b+1): # top to bottom
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1): # right to left
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1): # bottom to top
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res

        


if __name__ == '__main__':
    # ======= Test Case =======
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.spiralOrder(matrix)
    print(res)