class Solution:
    def maxProduct(self, n: int) -> int:
        b=str(n)
        n=list(map(int,b))
        max1=max(n)
        n.pop(n.index(max1))
        max2=max(n)
        return max1*max2