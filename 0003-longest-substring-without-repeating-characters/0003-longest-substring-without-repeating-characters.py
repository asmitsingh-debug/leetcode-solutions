class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dic={}
        total=0
        left=0
        right=0
        while right<len(s):
            if s[right] not in dic:
                dic[s[right]]=1
                total=max(total,right-left+1)
                right+=1
            else:
                del dic[s[left]]
                left+=1
        return total
                