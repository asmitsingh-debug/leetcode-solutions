# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        if n == count:
            return head.next

        k=0
        curr=head
        while curr:
            if k==count-n-1:
                temp=curr.next
                curr.next=curr.next.next
                temp.next=None
                break
            curr=curr.next
            k+=1
        return head
