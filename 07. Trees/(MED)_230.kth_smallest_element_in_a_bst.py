# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    # In-order traversal, O(n) time and space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]

        def dfs(root):
            if root.left:
                kth_value = dfs(root.left)
                
                if kth_value > -1:
                    return kth_value

            counter[0] += 1
            if counter[0] == k: # We found our value, we need to return it to the original root
                return root.val

            if root.right:
                kth_value = dfs(root.right)

                if kth_value > -1:
                    return kth_value

            return -1

        return dfs(root)

# Follow-up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, 
 # how would you optimize? Right now, you would have to keep traversing every node.
   
   # See .txt file

class IterativeSolution:
    # In-order traversal, O(n) time and space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            counter += 1

            if counter == k:
                return curr.val

            curr = curr.right
            