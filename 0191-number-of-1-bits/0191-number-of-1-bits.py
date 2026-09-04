class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0:
            if n%2==0:
                n=n//2
            else:
                c+=1
                n=n//2
        return c