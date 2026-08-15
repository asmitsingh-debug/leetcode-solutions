class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        ans=0

        if s[0].isalpha() :
            return 0
        if s[0]=='-':
            i=1
            while i < len(s) and s[i].isdigit():
                ans = ans * 10 + int(s[i])
                i+=1
            a=ans*(-1)
            if a<-2**31:
                return -2**31
            else:
                return a
        else:
            if s[0]=='+':
                i=1
            else:
                i=0
            while i < len(s) and s[i].isdigit():
                ans = ans * 10 + int(s[i])
                i+=1
            if ans>2**31 - 1:
                return 2**31 - 1
            else:
                return ans
            