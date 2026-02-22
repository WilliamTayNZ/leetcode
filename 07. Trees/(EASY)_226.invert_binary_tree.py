# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        right = root.right
        root.right = root.left
        root.left = right

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

# Works because we reliably handle null nodes
# Time complexity is O(n)
# In worst case, the recursion stack will have O(h) function calls where h is height of tree
  # With a perfectly balanced tree, this is log n
  # But since h could equal n, space complexity is O(n)


class IterativeSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        dq = deque([root])

        while dq:
            current = dq.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                dq.append(current.left)

            if current.right:
                dq.append(current.right)
        
        return root

# Queue is used to indicate *when* we should process (swap children of) each node (effectively a BFS)
# Time complexity is O(n)
# In worst case, queue will contain all nodes of the widest level of the binary tree
  # Or O(w) where w is the maximum width of the tree
  # In a full binary tree, this is ceil(n/2) so space complexity is O(n)

# January 4th, 2026