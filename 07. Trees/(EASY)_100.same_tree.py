# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# O(n) time complexity since each node is visited exactly once in worst case
# O(h) space complexity where h is the height of the tree
  # In worst case, h = n

class IterativeSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Run BFS on p and q at the same time
        dq = deque([(p, q)])

        while dq:
            p, q = dq.popleft()

            # If both are null
            if not p and not q:
                continue
            
            # If one is not null and other is null
            if not p or not q:
                return False
            
            # If both are not null but the values are not equal
            if p.val != q.val:
                return False
            
            dq.append((p.left, q.left)) # Append pair of p's left child and q's left child
            dq.append((p.right, q.right)) # Append pair of p's right child and q's right child

        return True

# O(n) time since each node is visited exactly once in worst case
# O(w) space where w is the max width of the tree
  # In worst case, where tree is a perfect fully balanced binary tree, the last level has ceil(n/2) nodes which is O(n) 