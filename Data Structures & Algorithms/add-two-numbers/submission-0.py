# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        l1_curr = l1
        l2_curr = l2
        new_head = ListNode()
        curr = new_head
        while carryover != 0 or (l1_curr is not None or l2_curr is not None):
            temp = 0
            if l1_curr is not None and l2_curr is not None:
                temp = l1_curr.val + l2_curr.val + carryover
                l1_curr = l1_curr.next
                l2_curr = l2_curr.next
            elif l1_curr is None and l2_curr is not None:
                temp = l2_curr.val + carryover
                l2_curr = l2_curr.next
            elif l1_curr is not None and l2_curr is None:
                temp = l1_curr.val + carryover
                l1_curr = l1_curr.next
            elif l1_curr is None and l2_curr is None:
                temp = carryover
            carryover = 0
            
            if temp / 10 >= 1:
                carryover = 1

            curr.next = ListNode()
            curr = curr.next
            curr.val = temp % 10

        return new_head.next