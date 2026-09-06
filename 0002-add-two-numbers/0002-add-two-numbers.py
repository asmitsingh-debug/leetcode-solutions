# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        l3=ListNode(None)
        head=l3
        cur3=l3
        cur1=l1
        cur2=l2
        while cur1 and cur2:
            total=cur1.val+cur2.val+carry
            if total>9:
                total=str(total)
                carry=int(total[0])
                if head.val is None:
                    head.val=int(total[1])
                else:
                    newnd=ListNode(int(total[1]))
                    cur3.next=newnd
                    cur3=cur3.next
            else:
                carry=0
                if head.val is None:
                    head.val=total
                else:
                    newnd=ListNode(total)
                    cur3.next=newnd
                    cur3=cur3.next
            cur1=cur1.next
            cur2=cur2.next
        if carry==1 and cur1 is None and cur2 is None:
            newnd=ListNode(1)
            cur3.next=newnd
            cur3=cur3.next
        if cur1:
            while cur1:
                total=cur1.val+carry
                if total>9:
                    total=str(total)
                    carry=int(total[0])
                    newnd=ListNode(int(total[1]))
                    cur3.next=newnd
                    cur3=cur3.next
                else:
                    carry=0
                    newnd=ListNode(total)
                    cur3.next=newnd
                    cur3=cur3.next
                cur1=cur1.next
            if carry==1:
                newnd=ListNode(1)
                cur3.next=newnd
                cur3=cur3.next
        if cur2:
            while cur2:
                total=cur2.val+carry
                if total>9:
                    total=str(total)
                    carry=int(total[0])
                    newnd=ListNode(int(total[1]))
                    cur3.next=newnd
                    cur3=cur3.next
                else:
                    carry=0
                    newnd=ListNode(total)
                    cur3.next=newnd
                    cur3=cur3.next
                cur2=cur2.next
            if carry==1:
                newnd=ListNode(1)
                cur3.next=newnd
                cur3=cur3.next
        return head