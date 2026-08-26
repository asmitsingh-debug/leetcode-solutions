class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        char=['a','e','i','o','u']
        count=0
        for i in range(k):
            if s[i] in char:
                count+=1
        total=count
        for i in range(k,len(s)):
            if s[i] in char:
                count+=1
            if s[i-k] in char:
                count-=1
            total=max(total,count)
        return total