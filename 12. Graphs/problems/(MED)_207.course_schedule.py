class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list

        # Run DFS through all courses (all nodes), since there may be unconnected components

        # In the DFS, if we encounter a node twice, we detect a cycle and return False

        # We use a seen set() to track whether a node has been visited


        adj = [[] for _ in range(numCourses)] # Use array since courses are indexess
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)

            
        def dfs(node):
            if not adj[node]:
                return

            if node in seen: # Cycle detected
                return True

            seen.add(node)
            
            for neighbour in adj[node]:
                if dfs(neighbour):
                    return True

            seen.remove(node)

            adj[node] = [] # We don't need to search this node anymore


        seen = set()
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
    
# Time complexity: O(m+n)
# Space complexity: O(m+n)