## Problem Statement

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

In other words, the max path sum from 1 node to another.


## Approach and Why

Similar to the Diameter problem (532), a key observation is that, since we can't use the same node twice, for any path sum, there can only be a maximum of ONE instance where the path moves from 1 child to its parent to its other child (crossing the parent if you will). 

This means that the rest of the max path sum (`mps`) path will consist of purely vertical movements. The `mps` path might also not contain any horizontal movements.

Now when we are at any node, we cannot know its `mps` without knowing how all its descendants contribute. This means we need all the necessary information about its left and right subtrees to determine its own `mps`. This screams post-order traversal `(left -> right -> root)`, in fact, it is required.

Hence, we do a DFS where we always start at the bottom of the left subtree. Similar to the Diameter problem, the `mps` of the tree could be the `mps` of any node down the tree. This means at each node we process, we could potentially update the global `mps`. 

As we go back up the tree, the information we really need to pass is the max path to root (mptr). This can be calculated with the equation `root_mptr = max(left_mptr, right_mptr, 0) + root.val`. The 0 is important because the mptr for both children could be negative, hence contributing negatively to the `mptr` (and by extension, the `mps`). Hence the 0 represents the choice **not to include a subtree** in the mptr.  

The `root_mps` can hence either be `left_mptr + right_mptr + root.val` or `root_mptr`. 

The base case, if not node, returns an mptr of 0.

## Key Pattern Takeaway

### The "Dual Role" Pattern
In complex tree problems, a recursive function often serves two purposes:
* **The Return Value:** Returning useful information to the parent
* **The Side Effect:** Updating a global variable to track a "curved" or "peaked" result that doesn't necessarily pass through the root.