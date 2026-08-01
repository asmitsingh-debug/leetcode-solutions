# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True