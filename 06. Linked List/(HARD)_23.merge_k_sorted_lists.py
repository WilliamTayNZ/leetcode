# Tricky problem: see the doc

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Array of linked-lists

        def merge_2_linked_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # Always O(V) where V is the total amount of nodes in list1 and list2
            dummy = ListNode(0, None)
            prev = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    prev.next = list1
                    prev = list1
                    list1 = list1.next
                else: # list1 > list2
                    prev.next = list2
                    prev = list2
                    list2 = list2.next

            prev.next = list2 if not list1 else list1

            return dummy.next


        while len(lists) > 1:
            k = len(lists)

            number_of_merged_lists = 0

            # Merge every 2 lists, except the final list if there was an odd number of lists
            # I did this in a way that saves maximum space, but a "cleaner" and easier way is to just make a new merged_lists array for each round of merging
              # You would have to handle the odd number of lists case in the for loop, which is pretty easy
            for i in range(0, k-1, 2): 
                merged = merge_2_linked_lists(lists[i], lists[i+1])
                lists[number_of_merged_lists] = merged 
                number_of_merged_lists += 1

            if k % 2 == 0:
                lists = lists[0:number_of_merged_lists]
            else: # when k is odd, append the skipped final list to the new lists
                last_list = lists[-1]
                lists = lists[0:number_of_merged_lists]
                lists.append(last_list)

        return None if not lists else lists[0]

# Overall time complexity is O(N log k) where N is the total number of nodes in all linked lists
# Space complexity is O(1) extra space

# January 7th, 2026