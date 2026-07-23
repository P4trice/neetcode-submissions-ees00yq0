"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        original = {} # old nodes in a list

        index_of = {}
        curr = head
        i = 0
        while curr is not None:
            original[i] = curr
            index_of[id(curr)] = i
            i += 1
            curr = curr.next

        copy = [Node(0) for _ in range(len(original))]

        for i in range(len(original)):
            if original[i].next != None:
                temp_next = index_of[id(original[i].next)]
                copy[i].next = copy[temp_next]

            if original[i].random != None:
                temp_random = index_of[id(original[i].random)]
                copy[i].random = copy[temp_random]

            copy[i].val = original[i].val
    
        return copy[0]