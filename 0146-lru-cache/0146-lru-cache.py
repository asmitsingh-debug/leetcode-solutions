class LRUCache:

    def __init__(self, capacity: int):
        self.lrucache=[]
        self.n=capacity

    def get(self, key: int) -> int:
        for i in range(0,len(self.lrucache)):
            if self.lrucache[i][0]==key:
                a=self.lrucache[i][1]
                self.lrucache.append((key,a))
                self.lrucache.pop(i)
                return a 
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.lrucache)):
            if self.lrucache[i][0] == key:
                self.lrucache.pop(i)
                break
        if len(self.lrucache)==self.n:
            self.lrucache.pop(0)
        self.lrucache.append((key,value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)