class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits="".join(list(map(str,digits)))
        a=int(digits)
        a+=1
        digits=list(map(int,str(a)))
        return digits