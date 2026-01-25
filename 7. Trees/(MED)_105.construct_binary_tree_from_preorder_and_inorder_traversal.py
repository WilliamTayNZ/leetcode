# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder: node, left, right
        # Inorder: left, node, right

        # 1. Create an item: index dict for inorder
        inorder_dict = {item : index for index, item in enumerate(inorder)}

        # Pre_idx of tree root
        self.pre_idx = -1
    
        def buildSubtree(left, right):
            # 1. Base case: if the window is empty, return None
            if left > right:
                return None

            # 2. Pick the current root using self.pre_idx and increment it
            self.pre_idx += 1

            # 3. Create the TreeNode
            root = TreeNode(preorder[self.pre_idx])

            # Find the new subtree's root's index in inorder
            inord_idx = inorder_dict[root.val]

            # 4. Recursively build root.left (using the left-of-root window)
            root.left = buildSubtree(left, inord_idx - 1)

            # 5. Recursively build root.right (using the right-of-root window)
            root.right = buildSubtree(inord_idx + 1, right)

            # 6. Return the root
            return root

        return buildSubtree(0, len(inorder) - 1)
    
# See (MED)_105.md for takeaways