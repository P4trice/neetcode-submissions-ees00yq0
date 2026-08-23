# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def checkAhead(self, head: Optional[ListNode], k: int) -> bool:
        if head is None:
            return False
        
        for i in range(k):
            if head is None:
                return False
            head = head.next

        return True

    def reverseKGroup(self, head, k):
        if head is None:
            return None
    
        anchor = ListNode(next=head)
        prev_tail = anchor   # durable pointer: last node of already-processed part
        group_start = head   # first node of the group 
    
        while self.checkAhead(group_start, k):
            prev = None # since we want to assign the last of the first group of k to None
            current = group_start
            for _ in range(k): # can use fixed for-loop since we know the numbers ahead
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            # after this: prev = new head of group, group_start = new tail of group,
            # current = first node of the NEXT group (or None)

            # variable clean-up/setup for next iteration
            prev_tail.next = prev        # previous segment now points at new head
            prev_tail = group_start      # this group's old head is now its tail
            group_start = current        # advance to the start of the next group
    
        # merge: prev_tail already correctly points at group_start (untouched remainder)
        # since we never touched prev_tail.next again if checkAhead failed
        prev_tail.next = group_start

        return anchor.next