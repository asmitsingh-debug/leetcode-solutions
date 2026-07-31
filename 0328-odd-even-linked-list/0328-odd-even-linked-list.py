# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        odd=head
        even=head.next
        codd=odd
        ceven=even
        while ceven and ceven.next:
            codd.next=ceven.next
            if ceven.next:
                ceven.next=ceven.next.next
            codd=codd.next
            ceven=ceven.next
        codd.next=even
        return head