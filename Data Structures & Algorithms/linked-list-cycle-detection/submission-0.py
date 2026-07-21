# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a hashmap of seen nodes, if you find a next that is in the list -> false. If you get to none -> true
        seen = []
        seen.append(head)
        if head is None:
            return False
        while head is not None:
            if head.next == None:
                return False
            if head.next in seen:
                return True
            seen.append(head.next)
            head = head.next

        return False