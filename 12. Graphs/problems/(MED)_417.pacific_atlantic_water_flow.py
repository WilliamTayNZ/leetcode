class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # The key to this problem is to realise that checking every cell is very inefficient
        # Instead, we should START from the oceans
         # This is because if we start at a cell, whatever result we end up with can only be applied to that cell
         # However, if we start from the ocean and work backwards, we already know that every cell we visit must be connected to the ocean


        # APPROACH

        # Run DFS on the starting pacific nodes, marking a node when it is seen as "pacific", visiting neighbours, progressing if neighbour's height >= pacific nodes
    
        # Run DFS on the starting atlantic nodes, marking a node when it is seen as "atlantic", visiting neighbours, progressing if neighbour's height >= atlantic nodes

        # Result will contain the nodes that are both pacific and atlantic



        # DFS Function
        def dfs(r,c, pacific):
            if pacific:
                seen = pacific_seen
            else:
                seen = atlantic_seen

            if (r,c) in seen:
                return
            seen.add((r,c))

            # Search north
            if r > 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1, c, pacific)

            # Search west
            if c > 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r, c-1, pacific)

            # Search south
            if r < m-1 and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, pacific)
            
            # Search east
            if c < n-1 and heights[r][c+1] >= heights[r][c]:
                dfs(r, c+1, pacific)

        m = len(heights)
        n = len(heights[0])

        # 1. Search pacific nodes
        pacific_seen = set()

        for r in range(m):
            dfs(r, 0, True)
        for c in range(n):
            dfs(0, c, True)
    
        # 2. Search atlantic nodes
        atlantic_seen = set()

        for r in range(m):
            dfs(r, n-1, False)
        for c in range(n):
            dfs(m-1, c, False)

        # 3. Add a node to result if it is in both pacific_seen and atlantic_seen
        result = []

        for r in range(m):
            for c in range(n):
                if (r,c) in pacific_seen and (r,c) in atlantic_seen:
                    result.append([r,c])

        return result
            