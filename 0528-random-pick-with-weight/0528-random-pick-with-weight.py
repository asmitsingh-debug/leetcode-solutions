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
        r_num=random.random()
        ind=r_num*self.total
        low=0
        high=len(self.prefix)-1
        while low<high:
            mid=low+(high-low)//2
            if ind>self.prefix[mid]:
                low=mid+1
            else:
                high=mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()