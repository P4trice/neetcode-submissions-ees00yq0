# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            suspect = head
            reverse = ListNode(val = head.val)
            while (suspect.next is not None):
                temp = ListNode(suspect.next.val)
                temp.next = reverse
                reverse = temp
                suspect = suspect.next
            
        return reverse