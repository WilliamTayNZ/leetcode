class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Another cycle detection problem

        # Create adjacency list (array) of edges
        # Iterate from node 0 to n-1, run DFS to detect a cycle

        # If the graph is not connected, its not a valid tree either


        # If an undirected graph has n nodes, n-1 edges and is connected, it must be a tree
        # So if it doesn't have n-1 edges, it's not a tree. 
          # Any less means it can't possibly be fully connected, any more means there MUST be a cycle
        if len(edges) != n-1:
            return False

        adj_list = [[] for _ in range(n)]
        
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = set()

        def dfs(i, parent=None):

            if i in seen:
                return False

            seen.add(i)

            for neighbour in adj_list[i]:
                if neighbour != parent: # Don't DFS the node's parent
                    if not dfs(neighbour, i):
                        return False

            # We don't remove node from seen set(), since in a valid tree we are only doing 1 DFS pass, so the only time we will see a node again is if there is a cycle.

            return True

        return dfs(0) and len(seen) == n
    
# Time complexity: O(N), technically O(N+E) but E <= N-1
# Space complexity: O(N), technically O(N+E) but E <= N-1