# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy.next
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            return None
        elif length == n:
            return dummy.next.next

        curr = dummy.next
        for i in range(length - n - 1):
            curr = curr.next
    
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return dummy.next

        
