from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(word, i, j):
            if not word:
                return True
            
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[0]:
                return
            
            board[i][j] = ''
            ops = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
            for op in ops:
                if dfs(word[1:], op[0], op[1]):
                    board[i][j] = word[0]
                    return True
            
            board[i][j] = word[0]
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, i, j):
                    return True                   

        return False


if __name__ == '__main__':
    # ======= Test Case =======
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    # ====== Driver Code ======
    sol = Solution()
    res = sol.exist(board, word)
    print(res)