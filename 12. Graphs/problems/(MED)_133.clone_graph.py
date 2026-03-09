# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Given node is always the node with index 0, val = 1
        # Vals are 1-indexes 

        # Constraint: could be 0 nodes in the graph
        if not node:
            return None


        # APPROACH: BFS

        # Pop ORIGINAL node from queue
        # If not in SEEN, Make a COPY node, add it to COPIES, then add ORIGINAL node to SEEN
        # Else, we use the existing COPY node equivalent

        # Check the original node's neighbors
        # If the ORIGINAL neighbor is in SEEN, we don't need to create or process the node since we already have done so. We just need to add the COPY neighbor to our COPY node's neighbors
        # Else, we should add the ORIGINAL neighbour to the queue, and create a COPY neighbor which is added to COPIES, that we add to COPY node's neighbors. Add ORIGINAL neighbour to SEEN

        dq = deque([node])
        copies = {}

        while dq:
            node = dq.popleft()

            if node.val not in copies:
                copies[node.val] = Node(node.val, [])
                copy_node = copies[node.val]
            else:
                copy_node = copies[node.val]
            
            for neighbor in node.neighbors:
                if neighbor.val in copies:
                    copy_node.neighbors.append(copies[neighbor.val])
                else:
                    dq.append(neighbor)
                    copies[neighbor.val] = Node(neighbor.val, [])
                    copy_node.neighbors.append(copies[neighbor.val])

        return copies.get(1)

# Time complexity: O(N+M)
# Space complexity: O(N)
