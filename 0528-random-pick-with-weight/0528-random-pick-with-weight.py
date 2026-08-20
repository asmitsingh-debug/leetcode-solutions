import random
class Solution:

    def __init__(self, w: List[int]):
        self.w=w
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)

        self.total = total
    def pickIndex(self) -> int:
        total=sum(self.w)
        r_num=random.random()
        ind=r_num*total
        for i in range(0,len(self.prefix)):
            if ind<=self.prefix[i]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()