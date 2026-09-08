class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        else:
            return 1*((n-1000)+1)