# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        i = 0
        anchor = ListNode(next = head)
        curr = anchor #start one before actual
        lag = anchor  #start one before actual
        while curr is not None and lag is not None:
            if i < n + 1:
                i += 1
            else:
                lag = lag.next
            curr = curr.next
        
        if lag is not None:
            if lag.next is not None:
                lag.next = lag.next.next


        print("i: " + str(i))
        if lag is not None:
            print("lag: " + str(lag.val))
        return anchor.next