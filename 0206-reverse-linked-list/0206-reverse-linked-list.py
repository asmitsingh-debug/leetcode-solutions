# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prv=head
        curr=prv.next
        head.next=None
        while curr!=None:
            temp=curr.next
            curr.next=prv
            prv=curr
            curr=temp
        head=prv
        return head