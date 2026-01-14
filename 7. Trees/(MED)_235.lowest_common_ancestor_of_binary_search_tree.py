# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # In a BST, every node's left child's value is smaller and right child's value is greater
        # This means that when finding 2 nodes p and q, as long as they are both smaller or greater than the current node in our search, we'll be taking the same path to find both of them
        # At some point, we may find a node which is greater than p or smaller than q, for example. This means we have to go 2 separate ways to find them. 
        # By definition, the last node before we go 2 separate ways must be the lowest common ancestor of both nodes
        # If one of our current node's children is p, this means p is an ancestor of q
        # If one of our current node's children is q, this means q is an ancestor of p

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

# O(n) time complexity since you can process every node
# O(1) space complexity since you only maintain one reference variable