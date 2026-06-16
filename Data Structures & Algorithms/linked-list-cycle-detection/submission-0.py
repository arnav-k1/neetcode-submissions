# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if (head == None):
            return False 

        if (head.next == None):
            return False
        if head.next.next == None:
            return False
        
        slow = head
        fast = head.next.next

        while fast != None:
            if fast.next == None or fast.next.next == None:
                return False

            if slow.next == fast.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False