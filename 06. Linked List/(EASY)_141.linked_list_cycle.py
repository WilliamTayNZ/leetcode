# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# The number of the nodes in the list is in the range [0, 104].
# Always be mindful of this (list can be empty)

# Intuitive solution: track nodes seen with indices and follow next pointer till a seen node is found
# But this is O(n) space, we want O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Two Pointers with Fast and Slow pointer
        # If the fast pointer laps the slow pointer, there is a cycle
        
        slow, fast = head, head

        # If there is ever a node whose next is None, there is no cycle
        # That's because this is a SINGLY linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True

        return False