class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        a=set()
        a.add(n)
        s=0
        while 1:
            if s==1:
                return True
            if n==0:
                n=s
                s=0
            while n!=0:
                ld=n%10
                s+=ld**2
                n=n//10
            if s in a:
                return False
            else:
                a.add(s)
                
