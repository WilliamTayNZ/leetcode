# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionRecursiveDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

# O(n) time
# O(n) space, specifically O(h) where h is maxDepth, and h <= n


class SolutionIterativeDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))

            max_depth = max(max_depth, depth)

        return max_depth

# Iterative DFS    
# Uses a stack to determine when we process each node, as well as the depth for each node
# For each node, push right child then left child (if they exist) with their depths
# O(n) time and O(n) space, specifically O(h) again 

# Iterative DFS solution does not have call stack overhead like Recursive DFS


class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0

        dq = deque([root])

        while dq:
            for i in range(len(dq)):
                curr = dq.popleft()

                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

            depth += 1

        return depth

# Key insight: When a level is just finished processing, the queue contains all nodes in the next level. Hence we use "for i in range(len(dq))" to pop (and process) the exact number of nodes in the next level.
# O(n) time, O(n) space i.e O(w) where width is maximum width of a level