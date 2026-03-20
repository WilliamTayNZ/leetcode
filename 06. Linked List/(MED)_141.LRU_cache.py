# A big takeaway: it's ok to use dummy nodes if they make the implementation cleaner.

# SOLUTION 1: LEETCODE EDITORIAL
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key: ListNode
        
        self.head = ListNode(-1, -1) 
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]

        # Move the node to the end of the linked list
        self.remove(node)
        self.add(node)

        return node.val

        
    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            old_node = self.hashmap[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.hashmap[key] = node
        self.add(node)

        if len(self.hashmap) > self.capacity:
            evicted = self.head.next
            self.remove(evicted)
            del self.hashmap[evicted.key]


    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# SOLUTION 2
# An earlier solution with less abstraction, and no dummy head and tail nodes
class ListNode:
    def __init__(self, key, value, prev: ListNode = None, next: ListNode = None):
        self.key = key
        self.value = value

        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key: ListNode
        
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hashmap:
            if self.tail.key == key:
                return self.hashmap[key].value

            node = self.hashmap[key]

            # move node to tail
            self.moveNodeToTail(node)
            
            return self.hashmap[key].value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:

        if len(self.hashmap) == 0:
            node = ListNode(key, value)
            self.tail, self.head = node, node
            self.hashmap[key] = node
        
        else:
            # If the key doesnt exist
            # Create a new ListNode, make it the new tail, update the hashmap
            if key not in self.hashmap:
                node = ListNode(key, value)
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                
                self.hashmap[key] = node

            # If the key exists, the key's node is moved to the tail
            else: 
                if self.tail.key == key:
                    self.hashmap[key].value = value
                    return

                # The node is definitely not the tail by this point
                node = self.hashmap[key]

                # Move node to tail
                self.moveNodeToTail(node)
                
                self.hashmap[key].value = value
        

        if len(self.hashmap) > self.capacity:
            # Evict the head of the linked list, and remove it from the dictionary   
            new_head = self.head.next
            new_head.prev = None

            # Remove it from the dictionary
            del self.hashmap[self.head.key]

            self.head = new_head

    def moveNodeToTail(self, node):
        node_prev = node.prev
        node_next = node.next # Always exists since node is not the tail

        if node_prev: # If node is not the head
            node_prev.next = node_next
        else:
            self.head = node_next
            
        node_next.prev = node_prev # None if this is the head, else it's node_prev
        
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node
