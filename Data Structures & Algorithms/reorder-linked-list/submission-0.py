# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        else:
            curr = head

        nodes = []
        while head is not None: 
            nodes.append(head)
            head = head.next

        new_head = curr
        # two-pointer approach
        i = 1
        j = len(nodes) - 1

        while i <= j:
            if i == j:
                curr.next = nodes[i]
                curr = curr.next
            else:
                curr.next = nodes[j]
                curr.next.next = nodes[i]
                curr = curr.next.next
                
            i += 1
            j -= 1


        curr.next = None

        head = new_head

