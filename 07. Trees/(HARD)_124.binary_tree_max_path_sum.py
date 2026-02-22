# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global_mps = [float(-inf)]

        # Bottom-up: You cannot know the max path at the root until you know the max contributions for the children

        # Three-Way decision: At each node,
        # 1. Is the best path going through me to my parent? (left/right -> root -> parent)
        # 2. Does the path stop at me?
        # 3. Is the best path going through me to my child? (right/left -> root -> left/right)

        def maxPathToRoot(root):
            if not root:
                return 0

            # mps: max_path_sum, mptr: max_path_to_root

            # Post order traversal (Left -> Right -> Root)

            left_mptr = maxPathToRoot(root.left)
            right_mptr = maxPathToRoot(root.right)

            root_mps = left_mptr + right_mptr + root.val 
            root_mptr = max(left_mptr, right_mptr, 0) + root.val # The decision. 0 if better not to inc. left or right mptr
            root_mps = max(root_mps, root_mptr)

            global_mps[0] = max(global_mps[0], root_mps)

            return root_mptr

        maxPathToRoot(root)

        return global_mps[0]

# O(n) time, O(h) space

