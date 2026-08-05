# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None

        # bruteforce would be to use list one as initial and then iterate
        # through all the other lists and insert their elements where needed
        # Space-Complexity: O(1) in additional space
        #
        # Time-Complexity: O(n*k)
        origin = None
        origin_temp = None

        for i in range(len(lists)):
            if origin is None: # should take care of multiple empty lists
                origin = lists[i]
                continue

            origin_temp = origin # need original reference to origin -> duplicate
            if lists[i] is None:
                continue
            list_head = lists[i]

            # original:  [1][2][4]
            # list_head: [1][3][5]
            # temp = [3]

            prev = None
            if origin_temp is not None:
                while list_head is not None:
                    if list_head.val <= origin_temp.val:
                        list_next = list_head.next
                        if prev is None:
                            origin = list_head
                            origin.next = origin_temp
                        else:
                            prev.next = list_head
                            list_head.next = origin_temp

                        prev = list_head
                        list_head = list_next
                        continue

                    if list_head.val > origin_temp.val:
                        if origin_temp.next is None:
                            origin_temp.next = list_head
                            break
                        else:
                            prev = origin_temp
                            origin_temp = origin_temp.next
                        continue
        return origin