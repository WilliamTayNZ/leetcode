# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The number of nodes in both lists is in the range [0, 50]

class IterativeSolution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Test case: list1 = [1,2,5], list2 = [3,4,6]

        dummy = ListNode()
        prev = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        
        if not list1:
            prev.next = list2
        else:
            prev.next = list1

        return dummy.next

class RecursiveSolution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Test case: list1 = [1,2,5], list2 = [3,4,5]
        # Think about the call stack i.e the flow of recursive calls

        # How do you break this down into smaller, identical subproblems?
        # At each stage, we are merging 2 smaller linked lists

        # What are the base cases?
        # When list1 is None or list2 is None

        # What does this function promise to return?
        # The head of the merged list

        # "The work is done on the way back"
        # i.e next pointers are changed after the recursive call returns
        # Visualisation is on tablet

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list2 = self.mergeTwoLists(list1.next, list2)
            list1.next = list2
            # This can be done in 1 line, but I find it easier to understand in 2
            return list1
        else: 
            list1 = self.mergeTwoLists(list1, list2.next)
            list2.next = list1
            # This can be done in 1 line, but I find it easier to understand in 2
            return list2

        # Don't forget to use self when recursively calling this function
        # Don't forget to use list.val too

# December 29th, 2025