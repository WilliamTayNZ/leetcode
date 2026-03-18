class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list with 2D array

        # 1 <= n <= 2000
        # 1 to 5000 edges

        # Iterate through all nodes as root nodes, running DFS on each
        # With DFS, we mark nodes as seen
        # When DFS is done on a root node, that's 1 component

        adj_list = [[] for _ in range(n)]
        for node, neighbour in edges:
            adj_list[node].append(neighbour)
            adj_list[neighbour].append(node)

        # For problems where nodes are indexed 0 to n-1, it's better to use an array instead of a set for seen
        seen = [False] * n 
        components = 0

        def dfs(node):
            if seen[node]:
                return

            seen[node] = True

            for neighbour in adj_list[node]:
                dfs(neighbour)


        for i in range(n):
            if not seen[i]:
                dfs(i)
                components += 1
            
        return components

# Time complexity: O(V+E)
# Space complexity: O(V+E) for adj_list (E) and seen (V)