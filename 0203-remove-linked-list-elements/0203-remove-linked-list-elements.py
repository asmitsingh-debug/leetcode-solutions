# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head and head.val == val:
            head = head.next

        if head is None:
            return None

        prv = head
        temp = head.next

        while temp:
            if temp.val == val:
                prv.next = temp.next
            else:
                prv = temp

            temp = temp.next

        return head