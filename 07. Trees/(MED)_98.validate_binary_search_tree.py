# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This problem is concerned with all nodes in a left subtree having lower values than the parent, and all nodes in a right subtree having higher values than the parent

# Key: notice and think critically about what values a node CANNOT take. 
   # What's the lowest and highest possible values any node can take?

class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float(-inf), high=float(inf)) -> bool:
        # When you travel down, there are bounds for how low or high a child can be
        # For left children, they need to all be lower than the parent value (high boundary)
        # For right children, they need to all be higher than the parent value (low boundary)

        if not root:
            return True
            
        if not (low < root.val < high):
            return False

        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)