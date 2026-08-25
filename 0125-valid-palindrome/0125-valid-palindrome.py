class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s :
            return False
        ans=''
        for char in s:
            if char.isalpha() or char.isdigit():
                ans+=char.lower()
        return ans==ans[::-1]