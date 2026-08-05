class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(indx,subset):
            if indx==len(digits):
                res.append("".join(subset))
                return
            for char in phone[digits[indx]]:
                subset.append(char)
                solve(indx+1,subset)
                subset.pop()
        subset=[]
        res=[]
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
        solve(0,subset)
        return res