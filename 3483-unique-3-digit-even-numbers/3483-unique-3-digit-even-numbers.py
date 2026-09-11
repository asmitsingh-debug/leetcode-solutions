import itertools
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        a=list(set(itertools.permutations(digits,3)))
        c=0
        for i in range(len(a)):
            if a[i][0] != 0 and a[i][-1] % 2 == 0:
                c+=1
        return c
