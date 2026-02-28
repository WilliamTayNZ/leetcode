class NeetCodeSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows_length = len(board)
        cols_length = len(board[0])
        
        path = set() # Helps us check if a node is already in our path

        def dfs(r, c, i):
            if i == len(word):
                return True

            # If our current node is not a valid choice
            if (r < 0 or c < 0 or r >= rows_length or c >= cols_length
                or board[r][c] != word[i] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            path.remove((r,c))

            return res

        i = 0 

        for r in range(rows_length):
            for c in range(cols_length):
                if dfs(r, c, i):
                    return True

        return False
    
class FirstSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = []
        visited: dict[tuple: bool] = {}

        res = [False]

        def explore(board, i, j):
            visited[(i,j)] = True

            if board[i][j] != word[len(path)-1]:
                return 
            else:
                if len(path) == len(word):
                    res[0] = True
                else:
                    if i > 0 and (i-1,j) not in visited:
                        path.append(board[i-1][j])
                        explore(board, i-1, j)
                        path.pop()
                        del visited[(i-1,j)]
                    if j > 0 and (i,j-1) not in visited:
                        path.append(board[i][j-1])
                        explore(board, i, j-1)
                        path.pop()
                        del visited[(i,j-1)]
                    if i < len(board) - 1 and (i+1,j) not in visited:
                        path.append(board[i+1][j])
                        explore(board, i+1, j)
                        path.pop()
                        del visited[(i+1,j)]
                    if j < len(board[i]) - 1 and (i,j+1) not in visited:
                        path.append(board[i][j+1])
                        explore(board, i, j+1)
                        path.pop()
                        del visited[(i,j+1)]

        # Loop 1: search through letters, row-by-row until you find the first letter
        for i in range(len(board)):
            for j in range(len(board[i])):
                letter = board[i][j]
                # If letter matches the first, start exploring..
                if letter == word[0]:
                    path.append(letter)
                    explore(board, i, j)
                    path.pop()
                    del visited[(i,j)]

                    if res[0] == True:
                        return True

        return False


        # Choosing whether to explore a direction

        # if i > 0, explore UP
        # if j > 0, explore LEFT
        # if i < len(board) - 1, explore DOWN
        # if j < len(row) - 1, explore RIGHT

        # For each case, make sure the node has not already been visited
