from typing import Optional


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, Node] = {}

        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        assert node.prev is not None and node.next is not None
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        assert self.head.next is not None
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        if len(self.map) >= self.capacity:
            lru_node = self.tail.prev
            assert lru_node is not None
            self._remove(lru_node)
            del self.map[lru_node.key]

        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_to_front(new_node)