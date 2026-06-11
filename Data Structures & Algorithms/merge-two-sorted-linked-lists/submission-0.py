# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        mergerStart = ListNode(0)
        merger = mergerStart

        while list1 and list2:

            if list1.val <= list2.val:
                #change pointers accordingly
                merger.next = list1
                list1 = list1.next
                merger = merger.next
            
            else:
                #change pointers accordingly
                merger.next = list2
                list2 = list2.next
                merger = merger.next

        merger.next = list1 if list1 else list2
        return mergerStart.next
