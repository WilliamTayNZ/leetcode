# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A useful thing to remember about level-by-level BFS is that whenever you finish processing nodes at depth i, what is left in your queue is every node at depth i+1
# This means you can use the size of your queue to determine how many nodes are at the next level
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        dq = deque([root])

        while dq:
            # Length of level to process
            q_length = len(dq)

            level = []

            # For each node in the level, add its value to the level array and enqueue any children
            for i in range(q_length):
                node = dq.popleft()
                
                level.append(node.val)
                
                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            levels.append(level)

        return levels

# O(n) time complexity
# O(w) space complexity where w is the maximum width (level with most nodes)