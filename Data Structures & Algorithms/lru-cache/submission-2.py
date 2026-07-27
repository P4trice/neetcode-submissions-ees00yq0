class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:

    # double linked list defines left as most recently used
    # hash-map is key -> node (by reference)
    def addNode(self, node: Node): # to Front (left)
        assert self.first.next is not None
        node.next = self.first.next
        node.prev = self.first
        self.first.next = node
        node.next.prev = node
        self.map[node.key] = node

    def removeNode(self, node: Node):
        assert node.prev is not None and node.next is not None
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # key -> Node (where key-value is stored)
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.removeNode(node)
        self.addNode(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        assert self.last.prev is not None
        # check if it already exists
            # update value + double linked list
        if self.capacity == 0:
            return
        if key in self.map:
            temp_node = self.map[key]
            temp_node.value = value
            self.removeNode(temp_node)
            self.addNode(temp_node)
        else:
            if(len(self.map) >= self.capacity):
                node_to_remove = self.last.prev
                self.removeNode(node_to_remove)
                self.map.pop(node_to_remove.key)
                
            temp_node = Node(key=key, value=value)
            self.map[key] = temp_node
            self.addNode(temp_node)
            

            
        # insert into hash-map
        # check if capacity is reached
        # insert into double list
        
