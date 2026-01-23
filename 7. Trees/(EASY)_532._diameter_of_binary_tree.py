# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, height = self.getCombinedHeightOfTwoSubtreesAndNodeHeight(root)
        print(f"diameter = {diameter}, height = {height}")
        return diameter

        # Run a depth first search recursively

        # From a bottom up perspective, everytime we go to a parent, we unlock a new pathway that could potentially give us the longest path between any two nodes in a tree.

        # Hence, we approach it from a bottom-of-the-tree up perspective: calculate the longest path unlocked, and compare it with the existing longest path i.e the existing diameter. 

        # So the DFS will visit each node, and each node will return its CH (for our diameter calculation) and height for the parent to use, to determine its own height AND its combined height

    
    def getCombinedHeightOfTwoSubtreesAndNodeHeight(self, root):
        combined_height, height, diameter = 0, 0, 0
        # For each node, we will calculate the CH for its left and right children if they exist

        # If the node's left or right child doesn't exist, it contributes nothing to height or diameter
        # So our base case is a node with no left or right child, hence the node has ch=0,h=0 and this is returned

        # If a node DOES have a left or a right child, it contributes to the node's height and diameter.
         # The node will call our function, which will return combined_height and height.
           # The node then uses combined_height to compare with existing diameter, and adds height to itself
        if root.left:
            child_diameter, child_height = self.getCombinedHeightOfTwoSubtreesAndNodeHeight(root.left)

            combined_height += child_height + 1
            left_height = child_height

            diameter = max(combined_height, child_diameter, diameter)


        if root.right:
            child_diameter, child_height = self.getCombinedHeightOfTwoSubtreesAndNodeHeight(root.right)
            
            combined_height += child_height + 1

            right_height = child_height

            diameter = max(combined_height, child_diameter, diameter)

        if root.left and not root.right:
            height += left_height + 1
        elif not root.left and root.right:
            height += right_height + 1
        elif root.left and root.right:
            height += max(left_height, right_height) + 1
        # If no child no change

        return (diameter, height)