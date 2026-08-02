class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        count=0
        curr=self.head
        while curr:
            if count==index:
                return curr.val
                break
            count+=1
            curr=curr.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_nd=Node(val)
        if self.head is None:
            self.head = new_nd
            return
        else:
            temp=new_nd
            new_nd.next=self.head
            self.head=temp
        return temp
    def addAtTail(self, val: int) -> None:
        new_nd=Node(val)
        if self.head is None:
            self.head = new_nd
            return
        else:
            curr=self.head 
            while curr.next is not None:
                curr=curr.next
            curr.next=new_nd
            return self.head

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            return self.addAtHead(val)
        new_nd=Node(val)
        count=0
        curr=self.head
        while curr:
            if count==index-1:
                temp=curr.next
                curr.next=new_nd
                new_nd.next=temp
                return self.head
            curr=curr.next
            count+=1
        else:
            return -1

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        while curr and curr.next:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)