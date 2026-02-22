# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CleanerSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        We can assume the linked list has no cycle.
        """

        # Step 1: Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        prev = slow.next
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next

class MyFirstSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        We can assume the linked list has no cycle.
        """

        # Lists of size 1 or 2 do not need to be reordered
        if not head.next or not head.next.next:
            return

        # Step 1: Use fast-and-slow to find the median
        slow, fast = head, head

        while fast and fast.next:
            if not fast.next.next: # ensures fast.next.next ends on the tail
                fast = fast.next 
            else:
                fast = fast.next.next

            slow = slow.next

        middle = slow
        tail = fast 

        # Case: 3 nodes
        # middle = node2, tail = node3

        # Case: 4 nodes
        # middle = node3, tail = node4

        # Case: 8 nodes
        # middle = node5, tail = node8

        # Case: 9 nodes
        # middle = node5, tail = node9


        # Step 2: Reverse second half of linked list starting from middle.next
        # See visualisations on tablet
        prev = middle
        curr = middle.next
        prev.next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # print(f"head after reversal: {head}")
        # print(f"tail after reversal: {tail}")


        # Step 3: Reorder

        # If we have even nodes, the head side is the last before reaching the middle
        # If we have odd nodes, the tail side is the last before reaching the middle
        left = head
        right_next = tail
        right = tail

        while left != None and right != None and left != middle and right != middle: # To mark end of reordering, and avoid errors
            left_next = left.next
            left.next = right_next
            left = left_next

            right_next = right.next
            right.next = left_next
            right = right_next

        middle.next = None # In some cases, we exit the while loop with middle.next = middle

# December 30th, 2025