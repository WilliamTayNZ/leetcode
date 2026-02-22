# The goal is not: "I solved it”
# The goal is: “I can now recognize this pattern when I see it again, and know why it works.”


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Constraints:
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Naive approach: Find end then count till n to the desired node
        # Our approach: LeadLag, use two pointers to represent an "interval" of size n
        #             When the pointer in front reaches the tail, we remove the other node

        dummy = ListNode(0, head)
        left, right = dummy, head

        # Create the interval between left and right
        for i in range(n-1): # n <= sz
            right = right.next

        # Move both pointers until right is at the tail
        while right.next:
            left = left.next
            right = right.next

        # Remove the node directly following left pointer
        left.next = left.next.next # note that here we can simply do this

        return dummy.next

# January 2nd, 2026
# solved in 18 mins yaya