class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through each row
        # For each row, run DFS on each element, checking if it is 1 (unseen), and if its neighbours are 1
        # To mark a node as seen, we can mark it as "0" to show we can't "reuse the land" (not a huge fan of this personally but it is an optimisation)
        # When a DFS run is completed, add 1 to the number of (weakly connected) components

        def dfs(i, j):
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            
            if i > 0:
                dfs(i-1, j)
            if i < len(grid) - 1:
                dfs(i+1, j)
            if j > 0:
                dfs(i, j-1)
            if j < len(grid[i]) - 1:
                dfs(i, j+1)

        components = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    components += 1

        return components

        # Time complexity: O(nm)